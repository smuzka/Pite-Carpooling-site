from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(models.Model):
    join_date = models.DateField(auto_now_add=True, blank=True)

    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    aboutme = models.TextField(blank=True, null=True, default=None)
    birth_date = models.DateField()

    email = models.EmailField()
    phone_number = PhoneNumberField(unique=True)

    passwd = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.lname} {self.fname}'

class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'

class Ride(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='driver')

    price = models.FloatField()
    seats_left = models.IntegerField()
    allow_pets = models.BooleanField()

    leave_date = models.DateTimeField()
    arrival_date = models.DateTimeField()

    begin_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='begin_city')
    end_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='end_city')

    passengers = models.ManyToManyField(User)
