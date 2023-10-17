from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    complement = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    cnpj = models.CharField(max_length=14)
    name = models.CharField(max_length=100)
    address = Address()

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)