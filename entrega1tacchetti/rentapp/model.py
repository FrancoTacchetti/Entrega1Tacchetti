import uuid
from django.db import models

class RentUsers(models.Model):
    PAID_CHOICES = (
        ("Cash", "Cash"),
        ("Credit/Debit Card", "Credit/Debit Card"),
        ("PayPal", "PayPal"),
    )
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    paid_method = models.CharField(max_length = 40, choices = PAID_CHOICES)
    rent_from = models.DateField()
    rent_to = models.DateField()
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class RentCar(models.Model):
    car_model = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    model_year = models.IntegerField()
    car_insurance = models.BooleanField()

class RentPlace(models.Model):
    location = models.CharField(max_length=40)
    rooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.BooleanField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    capacity = models.IntegerField()

