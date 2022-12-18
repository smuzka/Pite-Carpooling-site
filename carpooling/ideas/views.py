from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    return render(request, "homePage.html")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/logged")

        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request=request, template_name="loginPage.html", context={"login_form": form})


# TODO: match form fields in registerPage with UserForm
# TODO: override save method to save record to db
def register_request(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/logged")
    form = UserForm()
    return render(request=request, template_name="registerPage.html", context={"register_form": form})


def logout_request(request):
    logout(request)
    return redirect("/")


def profile(request):
    myContext = {"name": "Jacek Jackowski",
                "creationDate": "4 miesiące temu",
                "age" : "24",
                "phoneNumber": "123456789",
                "aboutMe": "Lorem Ipsum",
                "aboutCar": "Lorem Ipsum",
                "myRoutes": [{
                        "origin": "Krakow",
                        "destination": "Warszawa",
                        "date": "24.12.2022",
                        "hour": "17:00",
                        "carOwner": "Kapitan Bomba",
                        "seatsLeft": 2,
                    },
                    {
                        "origin": "Krakow",
                        "destination": "Warszawa",
                        "date": "24.12.2022",
                        "hour": "17:00",
                        "carOwner": "Kapitan Bomba",
                        "seatsLeft": 2,
                    }],
                "passengerRoutes": [{
                         "origin": "Krakow",
                         "destination": "Warszawa",
                         "date": "24.12.2022",
                         "hour": "17:00",
                         "carOwner": "Kapitan Bomba",
                         "seatsLeft": 2,
                    }]
   }

    return render(request=request, template_name="profilePage.html",
                  context=myContext)

def search(request):
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
    myContext = {}
    return render(request=request, template_name="newRoutePage.html", context=myContext)

