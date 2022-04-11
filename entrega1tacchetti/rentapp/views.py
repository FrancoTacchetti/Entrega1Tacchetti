from pickle import FALSE
from django.shortcuts import render
from multiprocessing import context

from django.views.generic import (
    TemplateView,
    ListView, 
    CreateView,
    DetailView)

from rentapp.models import (
    Tenant, 
    RentCar, 
    RentPlace)

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

def search(request):
        if request.method == "POST":
            search = request.POST["search"]
            if search != "":
                tenant_first_name = Tenant.objects.filter(first_name__contains=search)
                tenant_last_name = Tenant.objects.filter(last_name__contains=search)
                tenant_email = Tenant.objects.filter(email__contains=search)
                car_model = RentCar.objects.filter(car_model__contains=search)
                place_location = RentPlace.objects.filter(location__contains=search)

                searched = [
                    tenant_first_name,
                    tenant_last_name,
                    tenant_email,
                    car_model,
                    place_location
                ]

            else:
                searched = []

            context = {
                "search":search,
                "query": ""}

            try:
                for results in searched:
                    if results.exists():
                        query = results
                        context["query"] = query
                        break
                        # query = f"No Available Results For {search}"
                        # context["query"] = query
                        # context["no_results"] = True
            except:
                return render (request, template_name="500.html")
            print(context)
        return render(request,"rentapp/search_results.html", context=context)


