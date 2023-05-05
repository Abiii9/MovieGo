# Create your tests here.
from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from movie_go.models import Votes, Languages, Countries, Companies, Movies, Zones, Product, Customer, Order, Cart, LineItem
from movie_go.views.basic import get_from_model
from movie_go.views.dashboard import data_count, data_today
import ast
from faker import Faker
import datetime
class TempModelTest(TestCase):
    @classmethod
    #setting up the data for the Year and Temperature Models.
    def setUpTestData(cls):
        Votes.objects.create(vote_average= 6.7,vote_count = 89)
        Votes.objects.create(vote_average= 8.9,vote_count = 23)
        vote_obj1 = Votes.objects.get(id=1)
        vote_obj2 = Votes.objects.get(id=2)
        Languages.objects.create(spoken_languages="[{'iso_639_1': 'en', 'name': 'English'}]")
        Languages.objects.create(spoken_languages="[{'iso_639_1': 'it', 'name': 'Italiano'}]")
        lang_obj1 = Languages.objects.get(id=1)
        lang_obj2 = Languages.objects.get(id=2)
        Countries.objects.create(production_countries="[{'iso_3166_1': 'US', 'name': 'United States of America'}]")
        Countries.objects.create(production_countries="[{'iso_3166_1': 'NZ', 'name': 'New Zealand'}]")
        country_obj1 = Countries.objects.get(id=1)
        country_obj2 = Countries.objects.get(id=2)
        Companies.objects.create(production_companies="[{'name': 'Pixar Animation Studios', 'id': 3}]")
        Companies.objects.create(production_companies="[{'name': 'Warner Bros.', 'id': 6194}, {'name': 'Lancaster Gate', 'id': 19464}]")
        company_obj1 = Companies.objects.get(id=1)
        company_obj2 = Companies.objects.get(id=2)
        Movies.objects.create(belongs_to_collection="{'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}",budget=5000000,genres="[{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]",
        movie_id= 862, overview="Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.",
        popularity=21.946943, production_companies= company_obj1, production_countries= country_obj1,
        release_date= "30-10-1995",revenue=6000000,runtime = 135, spoken_languages= lang_obj1,
        tagline= " ",title="Toy Story", votes= vote_obj1,poster_path="/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg")
        Movies.objects.create(belongs_to_collection="{'id': 119050, 'name': 'Grumpy Old Men Collection', 'poster_path': '/nLvUdqgPgm3F85NMCii9gVFUcet.jpg', 'backdrop_path': '/hypTnLot2z8wpFS7qwsQHW1uV8u.jpg'}",budget=3000000,genres="[{'id': 10749, 'name': 'Romance'}, {'id': 35, 'name': 'Comedy'}]",
        movie_id= 15602, overview="A family wedding reignites the ancient feud between next-door neighbors and fishing buddies John and Max. Meanwhile, a sultry Italian divorcÃ©e opens a restaurant at the local bait shop, alarming the locals who worry she'll scare the fish away. But she's less interested in seafood than she is in cooking up a hot time with Max.",
        popularity=11.7129, production_companies= company_obj2, production_countries= country_obj2,
        release_date= "22-12-1995",revenue=5000000,runtime = 101, spoken_languages= lang_obj2,
        tagline= "Still Yelling. Still Fighting. Still Ready for Love.",title="Grumpier Old Men", votes= vote_obj2,poster_path="/nLvUdqgPgm3F85NMCii9gVFUcet.jpg")
        movie_obj1 = Movies.objects.get(id=1)
        movie_obj2 = Movies.objects.get(id=2)
        fake = Faker()
        Zones.objects.create(seats=5,screenwidth=40,aspect_ratio='16:9',resolution='2K',image='10_seater.jpg', address=fake.address(), cost= 80)
        zone_obj1 = Zones.objects.get(id=1)
        Product.objects.create(movie=movie_obj1,zone=zone_obj1,booking_date='2023-05-03', booking_time='23:59',price=7+zone_obj1.cost)
        product_obj1= Product.objects.get(id=1)
        Product.objects.create(movie=movie_obj2,zone=zone_obj1,booking_date='2023-05-01', booking_time='23:01',price=7+50)
        product_obj2= Product.objects.get(id=2)
        Cart.objects.create(product=product_obj1, quantity=3)
        cart_obj1 = Cart.objects.get(id=1)
        for i in range(5):
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
            customer = Customer.objects.get(user = user)
            customer.address = fake.address(),
            customer.address = str(customer.address[0])
            customer.save()
        customer_obj1 = Customer.objects.get(user_id=1)
        Order.objects.create(customer=customer_obj1)
        order_obj1 = Order.objects.get(id=1)
        LineItem.objects.create(quantity=3,product=product_obj2,cart = cart_obj1, order=order_obj1)

    def test_indexview(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie_go/index.html')
        self.assertContains(response, 'For a fantastic movie-watching experience')
    def test_get_from_model(self):
        product_obj1 = Product.objects.get(id=1)
        self.assertEqual(get_from_model(Product,1),product_obj1)
    def test_aboutview(self):
        client = Client()
        response = client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie_go/about.html')
        self.assertContains(response, 'This website was built using Django, which is an open-source framework for building web based applications in Python.')

    def test_moviesview(self):
        client = Client()
        response = client.get('/movies/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie_go/movies.html')
        self.assertContains(response, 'Search for a movie')
    def test_movies_post(self):
        client = Client()
        response = self.client.post('/movies/', {'movie': 'Toy Story'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie_go/movies.html')
        #print(response.content)
        #self.assertContains(response, 'Toy Story, vote: 7.7')
    def test_movie_details(self):
        client = Client()
        response = client.get('/movie_details/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie_go/movie_details.html')
        self.assertContains(response, "But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.")
    def test_zone_detail(self):
        client = Client()
        response = client.get('/zone_detail/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie_go/zone_detail.html')
        self.assertContains(response,'Number of seats: 5')
    def test_login(self):
        customer_obj1 = Customer.objects.get(user_id=1)
        login_url = '/accounts/login/'
        response = self.client.post(login_url, {'username': customer_obj1.user.username, 'password': 'p@ssw0rd'})
        self.assertEqual(response.url, '/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        response1 = self.client.get(response.url)
        self.assertContains(response1, f'Welcome back, {customer_obj1.user.first_name}')
    def test_purchase_without_login(self):
        response = self.client.get('/purchase/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/purchase/')
    def test_purchse_with_login(self):
        client = Client()
        customer_obj1 = Customer.objects.get(user_id=1)
        client.login(username=customer_obj1.user.username, password='p@ssw0rd')
        response = client.get('/purchase/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'You have these in your basket:')
    def test_payment(self):
        client = Client()
        customer_obj1 = Customer.objects.get(user_id=1)
        client.login(username=customer_obj1.user.username, password='p@ssw0rd')
        response = client.get('/payment/')
        self.assertEqual(response.status_code, 302)
        response1 = client.get(response.url)
        self.assertContains(response1, 'Congratulations! Your order has been placed')
    def test_order_list_without_login(self):
        client = Client()
        response = client.get('/user_order_list/')
        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(response.url, '/user_order_list/')
    def test_order_list_with_login(self):
        client = Client()
        customer_obj1 = Customer.objects.get(user_id=1)
        client.login(username=customer_obj1.user.username, password='p@ssw0rd')
        response = client.get('/user_order_list/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f'Order List for {customer_obj1.user.first_name}')
    def test_order_detail(self):
        client = Client()
        customer_obj1 = Customer.objects.get(user_id=1)
        client.login(username=customer_obj1.user.username, password='p@ssw0rd')
        response = client.get('/user_order/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The order includes these items')
    def test_product_list(self):
        client = Client()
        response = client.get('/product_list/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This is product 1 which costs\n       87.00')
    def test_product_detail(self):
        client = Client()
        response = client.get('/product/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Movie: Toy Story')
    def test_product_new(self):
        movie_obj1 = Movies.objects.get(id=1)
        zone_obj1 = Zones.objects.get(id=1)
        response = self.client.post(f'/product_new/{movie_obj1.id}/{zone_obj1.id}')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Product confirmation')
    def test_product_edit(self):
        client = Client()
        response = client.get('/product/1/edit/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Product confirmation')
    def test_product_delete(self):
        client = Client()
        response = client.get('/product/1/delete/')
        self.assertEqual(response.url, '/movies/')
        response1 = client.get(response.url)
        self.assertContains(response1, 'Search for a movie')
    def test_data_count(self):
        count = data_count(Product)
        self.assertEqual(count,2)
    def test_data_today(self):
        count_today = data_today(Customer)
        self.assertEqual(count_today, 5)
    def test_dashboard_with_customer(self):
        #client = Client()
        customer_obj1 = Customer.objects.get(user_id=1)
        self.client.login(username=customer_obj1.user.username, password='p@ssw0rd')
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 403)
    def test_basket_add(self):
        client = Client()
        response = client.post('/basket_add/1/')
        self.assertEqual(response.url, '/basket_detail/')
        response1 = client.get(response.url)
        self.assertContains(response1, 'You have these in your basket:')
    
    def test_basket_remove(self):
        client = Client()
        response = client.post('/basket_remove/1/')
        self.assertEqual(response.url, '/basket_detail/')
        response1 = client.get(response.url)
        self.assertContains(response1, 'Cart is empty')