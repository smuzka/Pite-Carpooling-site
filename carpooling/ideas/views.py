from django.shortcuts import render
from django.http import HttpResponse



def home(request):

    return (HttpResponse('<h1> Hello Django! </h1>'))

def login(request):
    return render(request, "loginPage.html")