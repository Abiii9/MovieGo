import os
import csv
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand,CommandError

from movie_go.models import Votes

class Command(BaseCommand):
    help = 'load data from csv'
    def handle(self, *args,**options):
        #drop data from tables
        Votes.objects.all().delete()
        print('tables dropped successfully')

        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir)+ '/movie_go/csv_data/Votes.csv', newline='') as f:
            reader = csv.reader(f, delimiter=',')
            next(reader)
            for row in reader:
                votes = Votes.objects.create(vote_average = float(row[0]), vote_count = int(row[1]))
                votes.save()

        print('data parsed successfully')
        