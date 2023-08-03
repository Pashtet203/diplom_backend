from django.db import models

class User(models.Model):
    Login = models.CharField(max_length=20)
    Email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

# Create your models here.
