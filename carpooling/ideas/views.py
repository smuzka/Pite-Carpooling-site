import datetime

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

from . import models
from .forms import UserForm, RideForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    return render(request, "homePage.html")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        for field in form:
            print("Field Error:", field.name, field.errors)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request=request, template_name="loginPage.html", context={"login_form": form})

def register_request(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
            user.save()
            user = authenticate(username=email, password=password)

            return HttpResponseRedirect("/")
    form = UserForm()
    return render(request=request, template_name="registerPage.html", context={"register_form": form})


def logout_request(request):
    logout(request)
    return redirect("/")


def profile(request):
    print(request.user)
    u = models.User.objects.get(email=request.user)
    print(u)
    name = u.first_name + " " + u.last_name

    today = datetime.date.today()
    age = today.year - u.birth_date.year - ((today.month, today.day) < (u.birth_date.month, u.birth_date.day))
    join_date = today - u.join_date

    myContext = {"name": name,
                "creationDate": join_date,
                "age" : age,
                "phoneNumber": u.phone_number,
                "aboutMe": u.about_me,
                "aboutCar": "Lorem Ipsum",
                "myRoutes": [{
                        "origin": "Krakow",
                        "destination": "Warszawa",
                        "date": "24.12.2022",
                        "hour": "17:00",
                        "carOwner": "Jacek Jackowski",
                        "seatsLeft": 2,
                        "isCarOwner": True,
                        "passengers": [{
                                "name": "Jacek",
                                "phoneNumber": "123456789",
                            },
                            {
                                "name": "Mietek",
                                "phoneNumber": "172938481",
                            },
                            {
                                "name": "Zdziś",
                                "phoneNumber": "987537952",
                            }],
                    },
                    {
                        "origin": "Warszawa",
                        "destination": "Krakow",
                        "date": "10.10.2022",
                        "hour": "17:00",
                        "carOwner": "Jacek Jackowski",
                        "seatsLeft": 2,
                        "isCarOwner": True,
                        "passengers": [],
                    }],
                "passengerRoutes": [{
                         "origin": "Mielno",
                         "destination": "Zamosc",
                         "date": "24.12.2022",
                         "hour": "17:00",
                         "carOwner": "Jacek Jackowski",
                         "seatsLeft": 4,
                         "isCarOwner": False,
                         "passengers": [{
                                    "name": "Kuba",
                                    "phoneNumber": "123456789",
                                },
                                {
                                    "name": "Też Kuba",
                                    "phoneNumber": "172938481",
                                }],
                         }],

   }

    return render(request=request, template_name="profilePage.html",
                  context=myContext)

def search(request):
    routes = []

    myContext = {
        "routes": [{
            "origin": "Krakow",
            "destination": "Warszawa",
            "date": "24.12.2022",
            "hour": "17:00",
            "carOwner": "Kapitan Bomba",
            "seatsLeft": 2,
        }]
    }

    return render(request=request, template_name="searchPage.html", context=myContext)

def new_route(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data.update({'driver' : [models.User.objects.get(email=request.user)]})
        print(data['driver'])
        form = RideForm(data)
        for field in form:
            print("Field Error:", field.name, field.errors)
        if form.is_valid():
            form.save()
    form = RideForm(initial= {'driver' : models.User.objects.get(email=request.user).pk})
    return render(request=request, template_name="newRoutePage.html", context={"ride_form" : form})

