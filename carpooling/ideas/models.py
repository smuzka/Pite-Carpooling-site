from django.db import models

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email = models.EmailField()
    passwd = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.lname} {self.fname}'

class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'

class Ride(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE)

    price = models.FloatField()
    seats_left = models.IntegerField()
    allow_pets = models.BooleanField()

    leave_date = models.DateTimeField()
    arrival_date = models.DateTimeField()

    begin_city = models.ForeignKey(City, on_delete=models.CASCADE)
    end_city = models.ForeignKey(City, on_delete=models.CASCADE)

    passengers = models.ManyToManyField(User)
