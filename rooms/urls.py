from django.urls import path

from .views import room_list, room_list_details

urlpatterns = [

    path("", room_list, name = "room_list"),

    path("room/<slug:room_slug>/", room_list_details, name = "room_list_details"),

]