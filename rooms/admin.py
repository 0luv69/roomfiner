from django.contrib import admin

# Register your models here.
from .models import Room, RoomImage


admin.site.register(Room)
admin.site.register(RoomImage)