import os
import csv
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand,CommandError
from faker import Faker
from movie_go.models import Zones
img_names = ['10_seater.jpg','5_seater.jpg', '8_seater.jpg','5_seater.jpg', '8_seater.jpg']
seats = [10,5,8,5,8]
screen_width = [60,40,50,40,50]
aspect_ratio = ['1:1.9','16:9','1:1.77','1:1.77','1:1.9']
resolution = ['4K','HD','2K','2K','4K']
cost = [90,40,60,50,80]
class Command(BaseCommand):
    help = 'load data from csv'
    def handle(self, *args,**options):
        #drop data from tables
        Zones.objects.all().delete()
        print('tables dropped successfully')
        fake = Faker()
        for i in range(5):
            zone = Zones.objects.create(seats = int(seats[i]),
            screenwidth = int(screen_width[i]),
            aspect_ratio = aspect_ratio[i],
            resolution = resolution[i],
            image = img_names[i],
            address = fake.address(),
            cost = float(cost[i]))
            zone.save()
        print('data parsed successfully')
        