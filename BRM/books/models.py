from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length = 50)
    price = models.FloatField()
    author = models.CharField(max_length = 50)
    publisher = models.CharField(max_length = 50)

class BookUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=False)
