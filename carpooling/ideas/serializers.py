from .models import User
def serialize(routes):
    return [{"origin": o.begin_city.name, "destination": o.end_city.name,
                    "date": o.leave_date.date().__str__(), "hour" : o.leave_date.time().__str__(),
                    "carOwner" : User.objects.get(id=o.driver_id), "seatsLeft" : o.seats_left, "isCarOwner" : True,
                    "passengers": [{"name" : p.first_name + " " + p.last_name, "phoneNumber": p.phone_number,} for p in o.passengers.all()]}
                     for o in routes]