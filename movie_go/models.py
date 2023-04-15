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

class Movies(models.Model):
    belongs_to_collection = models.TextField()
    budget = models.IntegerField()
    genres = models.TextField()
    movie_id = models.IntegerField()
    overview = models.TextField()
    popularity = models.FloatField()
    production_companies = models.ForeignKey(Companies, on_delete=models.CASCADE)
    production_countries = models.ForeignKey(Countries, on_delete=models.CASCADE)
    release_date = models.TextField()
    revenue = models.IntegerField()
    runtime = models.IntegerField()
    spoken_languages = models.ForeignKey(Languages, on_delete=models.CASCADE)
    tagline = models.TextField()
    title = models.TextField()
    votes = models.ForeignKey(Votes, on_delete=models.CASCADE)
    def __str__(self):
        return f'movie name: {self.title}, {self.release_date} '
    