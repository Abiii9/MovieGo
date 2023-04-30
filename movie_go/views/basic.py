from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from movie_go.models import Zones, Movies, Customer, Order, Product, Cart, LineItem
from movie_go.forms import SignUpForm
from movie_go.views.basket import Basket
import ast

genres = ['Animation', 'Comedy', 'Family', 'Adventure', 'Horror','Crime','Thriller','Drama','Fantasy']
movie_all = Movies.objects.all()
movie_names = [movie.title for movie in movie_all]

#helper functions
#get from models
def get_from_model(request,Model,id):
    if f'{Model}_obj' in request.session:
        obj = request.session[f'{Model}_obj']
    else:
        #fetching values from the  model.
        obj = Model.objects.get(id=id)
        request.session[f'{Model}_obj'] = obj 
    return obj
# Create your views here.
def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.customer.first_name = form.cleaned_data.get('first_name')
        user.customer.last_name = form.cleaned_data.get('last_name')
        user.customer.address = form.cleaned_data.get('address')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password= password)
        login(request, user)
        return redirect('/')
    return render(request, 'signup.html', {'form': form})
# index page view
def index(request):
    zones = Zones.objects.all()
    movies = Movies.objects.filter(votes__vote_average__gte=8).order_by('votes__vote_average')[:3]
    return render(request, 'movie_go/index.html', {'zones': zones, 'movies': movies})

def movies(request,genre = None):
    movies = Movies.objects.filter(votes__vote_average__gte=8).order_by('votes__vote_average')[:12]
    if request.method == 'POST':
        movie_name = request.POST.get('movie').strip()
        if movie_name != '':
            movies = Movies.objects.filter(title = movie_name)
    if genre:
        movies = Movies.objects.filter(genres__contains=genre)
    return render(request, 'movie_go/movies.html', {'movies': movies, 'movie_names': movie_names,'genres': genres})

def movie_details(request,id):
    movie = get_from_model(request,Movies,id)
    companies = eval(str(movie.production_companies))
    languages = eval(str(movie.spoken_languages))
    language_list = [language['name'] for language in languages]
    companies_list = [company['name'] for company in companies]
    return render(request, 'movie_go/movie_details.html',{'movie': movie, 'companies':', '.join(companies_list), 'languages': ', '.join(language_list)})

def zone_detail(request, movie_id):
    print(movie_id)
    movie = get_from_model(Movies,id)
    zones = Zones.objects.all()
    print(movie,zones)
    return render(request, 'movie_go/zone_detail.html',{'movie':movie,'zones': zones})

def purchase(request):
    if request.user.is_authenticated:
       user = request.user
       basket = Basket(request)
       
       return render(request, 'movie_go/purchase.html', {'basket': basket, 'user': user})
    else:
        return redirect('movie_go:login')

# save order, clear basket and thank customer
def payment(request):
    basket = Basket(request)
    user = request.user
    customer = get_object_or_404(Customer, user_id=user.id)
    order = Order.objects.create(customer=customer)
    order.refresh_from_db()
    for item in basket:
        product_item = get_object_or_404(Product, id=item['product_id'])
        cart = Cart.objects.create(product = product_item, quantity=item['quantity'])
        cart.refresh_from_db()
        line_item = LineItem.objects.create(quantity=item['quantity'], product=product_item, cart=cart,  order = order)

    basket.clear()
    request.session['deleted'] = 'thanks for your purchase'
    return redirect('movie_go:index' )

