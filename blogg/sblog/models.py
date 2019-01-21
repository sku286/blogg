from django.db import models
from rest_framework.serializers import (
    ModelSerializer,
     HyperlinkedModelSerializer
)
# Create your models here.
class Createdata(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    age = models.IntegerField()
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    timestamp = models.DateField()

    def __str__(self):
        return self.fname+self.lname




