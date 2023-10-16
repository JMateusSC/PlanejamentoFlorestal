from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

class Land(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateField()
    last_update_date = models.DateField()
    plots = models.FileField(upload_to="land_areas/")

