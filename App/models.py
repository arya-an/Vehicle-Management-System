from django.db import models
from django.contrib.auth.models import User

# Create your models here.
VEHICLE_TYPE_CHOICES=(
    ('Two Wheeler','Two Wheeler'),
    ('Three Wheeler','Three Wheeler'),
    ('Four Wheeler','Four Wheeler'),
)



class VehicleModel(models.Model):
    vehicle_number = models.CharField(max_length=30)
    vehicle_type = models.CharField(max_length=25, choices=VEHICLE_TYPE_CHOICES)
    vehicle_model = models.CharField(max_length=30)
    vehicle_description = models.CharField(max_length=30)
    