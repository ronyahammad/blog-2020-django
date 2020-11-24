from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist


class Profile(AbstractUser):
    
    ROLE_CHOICES=(
        ('Male','Male'),
        ('Female','Female'),
    )
    name=models.CharField(max_length=30, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=30,choices=ROLE_CHOICES, null=True, blank=True)
    
