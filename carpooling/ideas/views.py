import datetime

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from . import models
from .forms import UserForm, RideForm, SearchRouteForm
from .serializers import serialize

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
    u = models.User.objects.get(email=request.user)
    name = u.first_name + " " + u.last_name
    today = datetime.date.today()
    age = today.year - u.birth_date.year - ((today.month, today.day) < (u.birth_date.month, u.birth_date.day))
    join_date = today - u.join_date

    my_routes = models.Ride.objects.filter(driver_id=u.id)
    serialized_my_routes = serialize(my_routes)

    passenger_routes = models.Ride.objects.filter()
    myContext = {"name": name,
                "creationDate": join_date,
                "age" : age,
                "phoneNumber": u.phone_number,
                "aboutMe": u.about_me,
                "aboutCar": "Lorem Ipsum",
                "myRoutes": serialized_my_routes,
                "passengerRoutes": [{"origin": "Mielno","destination": "Zamosc",
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
    serialized_my_routes = []
    if request.method=="POST":
        form = SearchRouteForm(request.POST)
        if form.is_valid():
            origin = form.cleaned_data.get("origin")
            dest = form.cleaned_data.get("destination")

            routes = models.Ride.objects.filter(begin_city=origin, end_city=dest)
            serialized_my_routes = serialize(routes)

    form = SearchRouteForm()
    myContext = {
        "searchForm" : form,
        "routes": serialized_my_routes
    }
    return render(request=request, template_name="searchPage.html", context=myContext)

def new_route(request):
    driver_id = models.User.objects.get(email=request.user).id
    if request.method == 'POST':
        data = request.POST.copy()
        form = RideForm(data, driver_id=models.User.objects.get(email=request.user).id)
        for field in form:
            print("Field Error:", field.name, field.errors)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    form = RideForm(driver_id=driver_id)
    return render(request=request, template_name="newRoutePage.html", context={"ride_form" : form})

