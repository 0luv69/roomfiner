from django.shortcuts import render
from django.core.mail import send_mail
from .models import Room, RoomImage

# Create your views here.
def room_list(req):
    rooms = Room.objects.filter(is_available=True, is_active = True).prefetch_related("room_images")

    return render(req, "rooms_list.html", {"rooms": rooms})


def room_list_details(req, room_slug):
    particular_room = Room.objects.filter(slug = room_slug).first()

    return render(req, "rooms_details.html", {"room": particular_room})


