from django.contrib import admin
from .models import Tenant, RentPlace, RentCar, Post

# Register your models here.
admin.site.register(Tenant)
admin.site.register(RentPlace)
admin.site.register(RentCar)
admin.site.register(Post)

