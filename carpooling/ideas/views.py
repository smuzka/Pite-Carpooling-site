from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return render(request, "homePage.html")

def login(request):
    return render(request, "loginPage.html")

def register(request):
    return render(request, "registerPage.html")