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