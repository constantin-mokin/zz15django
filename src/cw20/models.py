from django.db import models

# Create your models here.

class Customer(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()
    proffesion = models.CharField(max_length=255)

