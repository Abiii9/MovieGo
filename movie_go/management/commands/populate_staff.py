"""
This file will populate the tables using Faker
"""
import random
import decimal
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from movie_go.models import StaffUsers


class Command(BaseCommand):
    help = 'Load data into the tables'

    def handle(self, *args, **options):
# drop the tables - use this order due to foreign keys - so that we can rerun the file as needed without repeating values
        print("tables dropped successfully")

        fake = Faker()

        # create some customers
        # we convert some values from tuples to strings
        for i in range(3):
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
            staffuser = StaffUsers.objects.get(user = user)
            staffuser.address = fake.address(),
            staffuser.address = str(staffuser.address[0])
            staffuser.is_staff = True
            staffuser.save()
        print("tables successfully loaded")