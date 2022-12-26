from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(models.Model):
    join_date = models.DateField(auto_now_add=True, blank=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    about_me = models.TextField(blank=True, null=True, default=None)
    birth_date = models.DateField(default='YYYY-MM-DD')
    profile_picture = models.ImageField(upload_to='pfps', null=True, blank=True)
    email = models.EmailField()
    phone_number = PhoneNumberField(unique=True, default="+48XXXXXXXXX")
    password = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'

class Ride(models.Model):
    driver_id = models.IntegerField(default=0)
    price = models.FloatField()
    seats_left = models.IntegerField()
    allow_pets = models.BooleanField(default=False)
    baby_seat = models.BooleanField(default=False)
    trunk = models.BooleanField(default=False)
    leave_date = models.DateTimeField(default='YYYY-MM-DD HH:MM')
    arrival_date = models.DateTimeField(default='YYYY-MM-DD HH:MM')
    begin_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='begin_city')
    end_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='end_city')
    passengers = models.ManyToManyField(User)

class CarBrand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    brand_id = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
