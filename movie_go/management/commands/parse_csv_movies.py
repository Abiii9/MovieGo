import os
import csv
import ast
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand,CommandError

from movie_go.models import Companies, Countries, Votes, Languages, Movies

class Command(BaseCommand):
    help = 'load data from csv'
    def handle(self, *args,**options):
        #drop data from tables
        Movies.objects.all().delete()
        print('tables dropped successfully')

        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir)+ '/movie_go/csv_data/moviess.csv', newline='') as f:
            reader = csv.reader(f, delimiter=',')
            next(reader)
            row_count = 0
            for row in reader:
                row_count +=1
                vote_obj = Votes.objects.get(id = row_count)
                company = row[6]
                company_obj = Companies.objects.get(production_companies = company)
                country = row[7]
                country_obj = Countries.objects.get(production_countries = country)
                language = row[11]
                language_obj = Languages.objects.get(spoken_languages = language)
                movie = Movies.objects.create(belongs_to_collection = row[0],
                budget = int(row[1]),
                genres = row[2],
                movie_id = int(row[3]),
                overview = row[4],
                popularity = float(row[5]),
                production_companies = company_obj,
                production_countries = country_obj,
                release_date = row[8],
                revenue = int(row[9]),
                runtime = int(row[10]),
                spoken_languages = language_obj,
                tagline = row[12],
                title = row[13],
                votes = vote_obj,
                poster_path = ast.literal_eval(row[0])['poster_path'])
                print(ast.literal_eval(row[0])['poster_path'])
                movie.save()

        print('data parsed successfully')