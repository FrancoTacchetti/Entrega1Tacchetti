from pickle import FALSE
from django.shortcuts import render
from multiprocessing import context
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import (
    UpdateView,
    TemplateView,
    ListView, 
    CreateView,
    DetailView,
    DeleteView)

from rentapp.models import (
    Tenant, 
    RentCar, 
    RentPlace,
    Post)

class FormsView():

    def __init__(self):
        self.creation_form = "rentapp/create_form.html"
        self.object_created = "rentapp/object_created.html"

class TenantCreateView(CreateView):
    template_name = FormsView().creation_form

    model = Tenant
    fields = [
            "first_name",
            "last_name",
            "email",
            "paid_method",
            "rent_from",
            "rent_to",
    ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_name"] = "Tenant"
        return context

class RentPlaceCreateView(CreateView):
    template_name = FormsView().creation_form

    model = RentPlace
    fields = [
            "location",
            "rooms",
            "bathrooms",
            "garage",
            "price",
            "capacity",
    ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_name"] = "Rentable Place"
        return context

class RentCarCreateView(CreateView):
    template_name = FormsView().creation_form

    model = RentCar
    fields = [
            "car_model",
            "price",
            "model_year",
            "car_insurance",
    ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_name"] = "Rentable Car"
        return context

class TenantDetailView(DetailView,TenantCreateView):
    template_name = "rentapp/detail_views/tenant_detail_view.html"

    model = Tenant

class PlaceDetailView(DetailView,RentPlaceCreateView):
    template_name = "rentapp/detail_views/place_detail_view.html"

    model = RentPlace

class CarDetailView(DetailView,RentCarCreateView):
    template_name = "rentapp/detail_views/car_detail_view.html"

    model = RentCar

def filter_search(searched_query):

    if searched_query != "":
        tenant_first_name = Tenant.objects.filter(first_name__contains=searched_query)
        tenant_last_name = Tenant.objects.filter(last_name__contains=searched_query)
        tenant_email = Tenant.objects.filter(email__contains=searched_query)
        car_model = RentCar.objects.filter(car_model__contains=searched_query)
        place_location = RentPlace.objects.filter(location__contains=searched_query)

        searched = [
            tenant_first_name,
            tenant_last_name,
            tenant_email,
            car_model,
            place_location
        ]

    else:
        searched = []
    
    return searched

def search_results(request):

        if request.method == "POST":
            search = request.POST["search"]

            context = {
            "search":search,
            "query": ""}

            searched = filter_search(search)

            try:
                for index, results in enumerate(searched):
                    if results.exists():
                        query = results
                        context["query"] = query
                        context["no_results"] = False
                        #This Logic Needs To Be Improved
                        #Logic Used Just to use one result view

                        if index == 0 or index == 1 or index == 2:
                            context["detail_view"] = "tenant-detail" 
                        elif index == 3:
                            context["detail_view"] = "car-detail" 
                        else:
                            context["detail_view"] = "place-detail" 
                        break

                    else:
                        query = f"No Available Results For {search}"
                        context["query"] = query
                        context["no_results"] = True
            except:
                return render (request, template_name="500.html")
            print(context)
        return render(request,"rentapp/search_results.html", context=context)

class PostListView(ListView):
    model = Post
    template_name = "rentapp/base.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post
    template_name = "rentapp/detail_views/post_detail_view.html"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    success_url = "/"
    template_name = "rentapp/post_form.html"
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "rentapp/post_form.html"
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "rentapp/post_confirm_delete.html"
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# def about(request):
#     return render(request, 'blog/about.html', {'title': 'About'})

