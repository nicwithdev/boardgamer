from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.


class Game(models.Model):
    name = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    players = models.IntegerField()
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Review(models.Model):
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    text = models.CharField(max_length=250)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)


class Wishlist(models.Model):
    name = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    players = models.IntegerField()
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
