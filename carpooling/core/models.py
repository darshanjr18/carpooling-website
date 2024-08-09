from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Route(models.Model):
    name = models.CharField(max_length=100, default='null')
    start_location = models.CharField(max_length=100, default='null')
    end_location = models.CharField(max_length=100, default='null')
    distance = models.DecimalField(max_digits=5, decimal_places=2, default='0')
    arrival_time = models.TimeField()  # Example field
    arrival_location = models.CharField(max_length=100)  # Example field
    departure_time = models.TimeField()  # Example field
    departure_location = models.CharField(max_length=100)  # Example field

    def __str__(self):
        return f"{self.name} ({self.start_location} to {self.end_location})"

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=20)
    vehicle_details = models.TextField(max_length=255, default='no details provided')

class Booking(models.Model):
  
    route = models.ForeignKey('Route', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    vehicle_details = models.CharField(max_length=255, default='no details avai')
    booking_time = models.DateTimeField(default='timezone.now')
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking {self.id} by {self.user}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    # Add other fields as needed

    def __str__(self):
        return self.user.username
