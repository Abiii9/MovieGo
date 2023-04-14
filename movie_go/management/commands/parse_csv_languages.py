import os
import csv
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand,CommandError

from movie_go.models import Languages

class Command(BaseCommand):
    help = 'load data from csv'
    def handle(self, *args,**options):
        #drop data from tables
        Languages.objects.all().delete()
        print('tables dropped successfully')

        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir)+ '/movie_go/csv_data/Languages.csv', newline='') as f:
            reader = csv.reader(f, delimiter=',')
            next(reader)
            for row in reader:
                language = Languages.objects.create(spoken_languages = row[0])
                language.save()

        print('data parsed successfully')