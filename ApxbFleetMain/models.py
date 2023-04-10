from django.db import models


class DriverLocation(models.Model):
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Driver Locations"


class Driver(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, default='')
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    car_make = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=20)
    picture = models.ImageField(
        upload_to='driver_pictures/', blank=True, null=True)
