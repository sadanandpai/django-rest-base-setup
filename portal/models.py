import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Fish(models.Model):
    
    Userid = models.ForeignKey(User, on_delete=models.CASCADE)
    Fishes = (
        ('BAN01', 'Bangade'),
        ('BUT02', 'Buthai'),
        ('MAN03', 'Manj'),
        ('PAM04', 'Pamplet'),
        ('ARK05', 'Arkoli'),
        ('KOK06', 'Kokkare'),
    )
    fishid = models.CharField(max_length=5, choices=Fishes)
    size = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    STATUS = (
        ('Active', 'active'),
        ('Inactive', 'inactive')
    )
    status = models.CharField(max_length=8, choices=STATUS)
    created_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_date']

    objects = models.Manager()
