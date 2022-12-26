from django.contrib import admin
from .models import User, City, Ride, CarBrand, CarModel

# Register your models here.
admin.site.register(User)
admin.site.register(City)
admin.site.register(Ride)
admin.site.register(CarBrand)
admin.site.register(CarModel)