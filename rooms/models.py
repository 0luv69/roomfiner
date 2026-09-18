from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string
# Create your models here.

class Room (models.Model):

    ROOM_TYPE = [
        ('single', "Single Rooms"),
        ('flat', "4 bhk Flat Rooms"),
        ('double', "Double Rooms"),
    ]

    ROOM_CATEGORY = [
        ('premium', "Premium Rooms"),
        ('standard', "Standard Rooms"),
        ('budget', "Budget Rooms"),
        ('hostel', "Hostel Rooms"),
        ('pg', "PG Rooms"),
        ('flat', "Flat Rooms"),
    ]

    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank= True)
    price = models.DecimalField(max_digits=10, decimal_places = 2)

    description = models.TextField()
    location = models.CharField(max_length=100)

    room_type = models.CharField(max_length=100, choices=ROOM_TYPE)
    category = models.CharField(max_length=100, choices=ROOM_CATEGORY)

    is_available = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} -- RS.{self.price} -- ({self.location})"


    def save(self, *args, **kwargs):
        # Generate slug before saving if it doesn't exist
        if not self.slug:
            self.slug = f"{slugify(self.title)}-{get_random_string(3)}"
        super().save(*args, **kwargs)



class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_images')
    image = models.ImageField(upload_to="room_img/")
    order= models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.room.title}  -- IMG ({self.order})"

