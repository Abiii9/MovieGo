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
    poster_path = models.TextField(null=True)
    def __str__(self):
        return f'movie name: {self.title}, {self.release_date} '
    
class Zones(models.Model):
    seats = models.IntegerField()
    screenwidth = models.IntegerField()
    aspect_ratio = models.TextField()
    resolution = models.TextField()
    image = models.TextField()
    address = models.TextField()
    cost = models.FloatField()
    def __str__(self):
        return f'{self.seats}, {self.cost}'

#shopping models
class Cart(models.Model):
    product = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='carts')
    quantity = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.product},{self.quantity},{self.created_date}'

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    address = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.email}, {self.address}'

    class Meta:
        db_table = 'customer'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Customer.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.customer.save()

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer},{self.created_date}'
class LineItem(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(Movies, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity},{self.product},{self.cart},{self.order},{self.created_date}'

