from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    ''''''





class Hall(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Place(models.Model):
    #name = models.CharField(max_length=100)
    number = models.IntegerField()
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)



class Event(models.Model):
    date = models.DateTimeField()


class Booking(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)


