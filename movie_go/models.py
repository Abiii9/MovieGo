# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Votes(models.Model):
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    def __str__(self):
        return f'average: {self.vote_average}, number of votes: {self.vote_count}'


class Languages(models.Model):
    spoken_languages = models.TextField()
    def __str__(self):
        return f'{self.spoken_languages}'

class Countries(models.Model):
    production_countries = models.TextField()
    def __str__(self):
        return f'{self.production_countries}'

class Companies(models.Model):
    production_companies = models.TextField()
    def __str__(self):
        return f'{self.production_companies}'    
