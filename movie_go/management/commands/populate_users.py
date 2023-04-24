import datetime
from django.db import models
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from movie_go.models import Customer
from faker import Faker

class Command(BaseCommand):
    help = 'Load data into the tables'
    def handle(self, *args, **options):
        fake = Faker()
        # create some customers in the past
        # we convert some values from tuples to strings
        for i in range(10):
            first_name = fake.first_name(),
            first_name = str(first_name[0])
            last_name = fake.last_name(),
            last_name = str(last_name[0])
            username = first_name + last_name,
            username = username[0]
            user = User.objects.create_user(
            username = username,
            first_name = first_name,
            last_name = last_name,
            email = fake.ascii_free_email(), 
            password = 'p@ssw0rd')
            customer = Customer.objects.get(user = user)
            customer.address = fake.address(),
            customer.address = str(customer.address[0])
            customer.created_date = datetime.datetime(2023, 4, 3, 21, 39, 33, 936978, tzinfo=datetime.timezone.utc)
            customer.save()