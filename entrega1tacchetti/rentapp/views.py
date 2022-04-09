from django.shortcuts import render
from multiprocessing import context
from django.views.generic import (
    TemplateView,
    ListView, 
    CreateView)
from .models import (
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

class RentCarCreateView(CreateView):
    model = RentCar
    fields = [
            "car_model",
            "price",
            "model_year",
            "car_insurance",
        ]



