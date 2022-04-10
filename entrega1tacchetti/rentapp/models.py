import uuid
from django.db import models
from django.urls import reverse
from django.utils import timezone

class Tenant(models.Model):
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
    date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("tenant-cretion-detail", kwargs={"pk": str(self.uuid)})
    
class RentCar(models.Model):
    car_model = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    model_year = models.IntegerField()
    car_insurance = models.BooleanField()
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"{self.car_model}"
    
    def get_absolute_url(self):
        return reverse("car-cretion-detail", kwargs={"pk": str(self.pk)})

class RentPlace(models.Model):
    location = models.CharField(max_length=40)
    rooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    garage = models.BooleanField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    capacity = models.PositiveIntegerField()
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"{self.location}"
    
    def get_absolute_url(self):
        return reverse("place-cretion-detail", kwargs={"pk": str(self.uuid)})

