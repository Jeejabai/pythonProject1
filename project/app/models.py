from django.db import models

class Form(models.Model):
    name = models.CharField(max_length=10)
    mobile = models.IntegerField()
    address = models.CharField(max_length=20)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=10)

class Login(models.Model):
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=10)
    type = models.IntegerField()

class Product(models.Model):
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    model = models.CharField(max_length=20)
    des = models.CharField(max_length=25)
    img = models.FileField()

