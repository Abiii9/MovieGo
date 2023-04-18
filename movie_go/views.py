from django.shortcuts import render, get_object_or_404
from .models import Zones, Movies
import ast
# Create your views here.
# index page view
def index(request):
    zones = Zones.objects.all()
    movies = Movies.objects.filter(votes__vote_average__gte=8).order_by('votes__vote_average')[:5]
    collection = [ast.literal_eval(movie.belongs_to_collection) for movie in movies]
    return render(request, 'movie_go/index.html', {'zones': zones, 'movies': movies})
