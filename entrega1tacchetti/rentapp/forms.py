from django import forms
from .models import Tenant, RentCar, RentPlace

# ModelForm to create a Form class from a Django model
class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant  
        fields = [
            "first_name",
            "last_name",
            "email",
            "paid_method",
            "rent_from",
            "rent_to",
        ]

class RentCarForm(forms.ModelForm):
    class Meta:
        model = RentCar
        fields = [
            "car_model",
            "price",
            "model_year",
            "car_insurance",
        ]

class RentPlaceForm(forms.ModelForm):
    class Meta:
        model = RentPlace
        fields = [
            "location",
            "rooms",
            "bathrooms",
            "garage",
            "price",
            "capacity",
        ]
