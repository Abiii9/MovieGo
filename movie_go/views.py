from django.shortcuts import render, get_object_or_404
from .models import Zones, Movies
import ast
genres = ['Animation', 'Comedy', 'Family', 'Adventure', 'Horror','Crime','Thriller','Drama','Fantasy']
movie_all = Movies.objects.all()
movie_names = [movie.title for movie in movie_all]
# Create your views here.
# index page view
def index(request):
    zones = Zones.objects.all()
    movies = Movies.objects.filter(votes__vote_average__gte=8).order_by('votes__vote_average')[:3]
    return render(request, 'movie_go/index.html', {'zones': zones, 'movies': movies})

def movies(request,genre = None):
    movies = Movies.objects.filter(votes__vote_average__gte=8).order_by('votes__vote_average')[:12]
    print(movies)

    if request.method == 'POST':
        movie_name = request.POST.get('movie').strip()
        if movie_name != '':
            movies = Movies.objects.filter(title = movie_name)
    if genre:
        movies = Movies.objects.filter(genres__contains=genre)
    return render(request, 'movie_go/movies.html', {'movies': movies, 'movie_names': movie_names,'genres': genres})

def product_details(request,id):
    movie = Movies.objects.get(id=id)
    companies = eval(str(movie.production_companies))
    languages = eval(str(movie.spoken_languages))
    language_list = [language['name'] for language in languages]
    companies_list = [company['name'] for company in companies]
    return render(request, 'movie_go/product_details.html',{'movie': movie, 'companies':', '.join(companies_list), 'languages': ', '.join(language_list)})