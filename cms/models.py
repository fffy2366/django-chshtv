from django.db import models
#from django
from django.contrib import auth

# Create your models here.
class Admin(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)