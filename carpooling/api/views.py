from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from .serializers import TodoSerializer

from .models import Todo
# Create your views here.


class TodoListView(generics.ListAPIView):
    model = Todo
    serializer_class = TodoSerializer


def home(request):

    return (HttpResponse('<h1> Hello Django! </h1>'))

def login(request):
    return render(request, "loginPage.html")