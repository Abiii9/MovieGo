from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from movie_go.models import Zones, Movies, Customer, Order, Product, Cart, LineItem
from movie_go.forms import SignUpForm
from movie_go.views.basket import Basket
import ast

genres = ['Animation', 'Comedy', 'Family', 'Adventure', 'Horror','Crime','Thriller','Drama','Fantasy']
movie_all = Movies.objects.all()
movie_names = [movie.title for movie in movie_all]

#helper functions
#get from models.
def get_from_model(Model,id):
    obj = Model.objects.get(id=id)
    return obj

# Create your views here.
#view for new customer signup.
def signup(request):
    try:
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            #using the data fetched from the form to create user account
            user.customer.first_name = form.cleaned_data.get('first_name')
            user.customer.last_name = form.cleaned_data.get('last_name')
            user.customer.address = form.cleaned_data.get('address')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            #using the in-built authentication method for authenticating the new user
            user = authenticate(username=username, password= password)
            #logging in the new user
            login(request, user)
            return redirect('/')
        return render(request, 'signup.html', {'form': form})
    except:
        return render(request, 'movie_go/500.html')
# index page view
#homepage that contains all the basic information about the application.
def index(request):
    try:
        zones = Zones.objects.all()
        movies = movie_all.filter(votes__vote_average__gte=8).order_by('votes__vote_average')[:3]
        return render(request, 'movie_go/index.html', {'zones': zones, 'movies': movies})
    except:
        return render(request, 'movie_go/500.html')
#about page that contains a detailed overview of the application.
def about(request):
    try:
        return render(request, 'movie_go/about.html')
    except:
        return render(request, 'movie_go/500.html')

#the movies page that lets user search and view general information about movies.
def movies(request,genre = None):
    try:
        no_movies = None
        #displaying top-rated movies first
        movies = movie_all.filter(votes__vote_average__gte=8).order_by('votes__vote_average')[:12]
        if request.method == 'POST':
            #getting the searched movie name from user
            movie_name = request.POST.get('movie').strip()
            if movie_name != '':
                #fetching the movie searched by the user
                movies = movie_all.filter(title=movie_name)
                if not movies:
                    #incase no movie was found, convey the same to the user
                    no_movies = f'No results for {movie_name}. Try checking the spelling'
        #if the user clicks on a genre, display movies accordingly
        if genre:
            movies = movie_all.filter(genres__contains=genre)
        return render(request, 'movie_go/movies.html', {'movies': movies, 'movie_names': movie_names,'genres': genres, 'no_movies': no_movies})
    except:
        return render(request, 'movie_go/500.html')

#displays in-detail information about the movie selected by the user from the movies page.
def movie_details(request,id):
    try:
        movie = get_from_model(Movies,id)
        companies = eval(str(movie.production_companies))
        languages = eval(str(movie.spoken_languages))
        language_list = [language['name'] for language in languages]
        companies_list = [company['name'] for company in companies]
        return render(request, 'movie_go/movie_details.html',{'movie': movie, 'companies':', '.join(companies_list), 'languages': ', '.join(language_list)})
    except:
        return render(request, 'movie_go/500.html')

#displays in-detail information about all the zones present for the user to select.
def zone_detail(request, movie_id):
    try:
        movie = get_from_model(Movies,movie_id)
        zones = Zones.objects.all()
        return render(request, 'movie_go/zone_detail.html',{'movie':movie,'zones': zones})
    except:
        return render(request, 'movie_go/500.html')


#allows the user to check and purchase the contents of his/her basket.
@login_required(login_url='movie_go:login')
def purchase(request):
    try:
        user = request.user
        basket = Basket(request)
        return render(request, 'movie_go/purchase.html', {'basket': basket, 'user': user})
    except:
        return render(request, 'movie_go/500.html')

# allows user to create an order and delete the basket session.
def payment(request):
    try:
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
        return redirect('movie_go:success', id=order.id )
    except:
        return render(request, 'movie_go/500.html')

#displays order success information to the user
def success(request,id):
    try:
        order = Order.objects.get(id=id)
        lineitems = LineItem.objects.filter(order=order)
        return render(request, 'movie_go/success.html', {'order': order, 'lineitems': lineitems})
    except:
        return render(request, 'movie_go/500.html')

#function that gets called incase of a 404 page not found error.
def error_404_view(request, exception):
    return render(request, 'movie_go/404.html', status=404)
#function that gets called incase of a 500 internal server error.
def error_500_view(request):
    return render(request, 'movie_go/500.html', status=500)
#function that gets called incase of a 403 forbidden error.
def error_403_view(request, exception):
    return render(request, 'movie_go/403.html', status=403)