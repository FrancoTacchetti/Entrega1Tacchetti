from django.shortcuts import render
from multiprocessing import context
from django.views.generic import (
    TemplateView,
    ListView, 
    CreateView)
from rentapp.models import (
    Tenant, 
    RentCar, 
    RentPlace)


class HomeView(TemplateView):

    # Redirect To Other Views
    pass

class TenantCreateView(CreateView):
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



