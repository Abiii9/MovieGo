import random
import decimal
import datetime
from django.db import models
from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from movie_go.models import Order, Customer

class Command(BaseCommand):
    help = 'Load data into the tables'

    def handle(self, *args, **options):
        customers = Customer.objects.all()[:5]
        for customer in customers:  
            for i in range(3):
                order = Order.objects.create(
                customer = customer,
                created_date = datetime.datetime(2023, 1, 9, 21, 39, 33, 936978, tzinfo=datetime.timezone.utc)
                )
                order.save()