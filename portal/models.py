import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
Fishes = (
     ('BAN01', 'Bangade'),
     ('BUT02', 'Buthai'),
     ('MAN03', 'Manj'),
     ('PAM04', 'Pamplet'),
     ('ARK05', 'Arkoli'),
     ('KOK06', 'Kokkare'),
)
Status = (
     ('Active', 'Active'),
     ('Inactive', 'Inactive'),
)
class Fish(models.Model):
    Userid = models.ForeignKey(User, on_delete=models.CASCADE)
    fish_id = models.CharField(max_length=5, choices=Fishes)
    size = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    status = models.CharField(max_length=8, choices=Status)
    created_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now=True)
