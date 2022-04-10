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

class TenantCreateView(CreateView,FormsView):
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

class TenantDetailView(DetailView):
    template_name = FormsView().object_created

    model = Tenant

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_name"] = "Tenant"
        return context

class PlaceDetailView(DetailView):
    template_name = FormsView().object_created

    model = RentPlace

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_name"] = "Rentable Place"
        return context

class CarDetailView(DetailView):
    template_name = FormsView().object_created

    model = RentCar

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_name"] = "Rentable Car"
        return context


