import os
import csv
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand,CommandError

from movie_go.models import Companies

class Command(BaseCommand):
    help = 'load data from csv'
    def handle(self, *args,**options):
        #drop data from tables
        Companies.objects.all().delete()
        print('tables dropped successfully')

        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir)+ '/movie_go/csv_data/Companies.csv', newline='') as f:
            reader = csv.reader(f, delimiter=',')
            next(reader)
            for row in reader:
                company = Companies.objects.create(production_companies = row[0])
                company.save()

        print('data parsed successfully')