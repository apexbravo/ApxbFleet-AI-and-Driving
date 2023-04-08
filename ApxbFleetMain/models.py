from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class Driver(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, default='')
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    car_make = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=20)
    location_lat = models.DecimalField(
        max_digits=9, decimal_places=6, default=0)
    location_long = models.DecimalField(
        max_digits=9, decimal_places=6, default=0)
    picture = models.ImageField(
        upload_to='driver_pictures/', blank=True, null=True)
