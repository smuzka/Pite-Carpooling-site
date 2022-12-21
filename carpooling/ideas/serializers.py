from .models import User, Ride

def passenger_already(route, user):
    u_id = User.objects.get(email=user).id
    for p in route.passengers.all():
        if p.id == u_id:
            return True
    return False

def is_driver(route, user):
    u_id = User.objects.get(email=user).id
    print(u_id)
    if u_id == route.driver_id:
        return True
    return False
def serialize_routes(routes, request):
    url = request.path
    crr_user_id = User.objects.get(email=request.user).id
    return [{"id": o.id,"origin": o.begin_city.name, "destination": o.end_city.name,
                    "date": o.leave_date.date().__str__(), "hour" : o.leave_date.time().__str__(),
                    "carOwner" : User.objects.get(id=o.driver_id), "seatsLeft" : o.seats_left,
                    "canSign" : o.seats_left <= 0 or passenger_already(o,request.user) or is_driver(o, request.user),
                    "passengers": [{"name" : str(p), "phoneNumber": p.phone_number, "id": p.id} for p in o.passengers.all()]}
                     for o in routes]

