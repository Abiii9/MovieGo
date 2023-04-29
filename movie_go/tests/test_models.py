from django.test import Client, TestCase
from django.contrib.auth.models import User
from movie_go.models import Votes, Languages, Countries, Companies, Movies, Zones, Product, Customer, Order, Cart, LineItem
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
    def test_votes(self):
        vote = Votes.objects.get(id=1)
        self.assertEqual(vote.vote_average,6.7)
    def test_languages(self):
        language = Languages.objects.get(id=1)
        self.assertIn('English', language.spoken_languages)
    def test_countries(self):
        country = Countries.objects.get(id=2)
        country_dict = eval(str(country.production_countries))
        self.assertEqual('New Zealand', country_dict[0]['name'])
    def test_companies(self):
        company = Companies.objects.get(id=1)
        company_dict = eval(str(company.production_companies))
        self.assertEqual('Pixar Animation Studios', company_dict[0]['name'])
    def test_movies(self):
        country_obj2 = Countries.objects.get(id=2)
        movie = Movies.objects.get(votes__vote_average__gte=7)
        self.assertTrue(movie)
        self.assertEqual("Grumpier Old Men", movie.title)
        self.assertEqual(movie.production_countries, country_obj2)
    def test_zones(self):
        zone = Zones.objects.get(id=1)
        self.assertEqual('16:9', zone.aspect_ratio)
    def test_product(self):
        product1 = Product.objects.get(id=1)
        self.assertTrue(product1.created_date)
        self.assertEqual(87.0, product1.price)
    def test_cart(self):
        cart = Cart.objects.get(id=1)
        self.assertTrue(cart.created_date)
        self.assertEqual(cart.product.movie.runtime, 135)
    def test_customer(self):
        customer = Customer.objects.get(user_id=1)
        self.assertIsInstance(customer.user, User)
    def test_order(self):
        order = Order.objects.get(id=1)
        self.assertTrue(order.created_date)
        self.assertEqual(str(order.created_date)[:10], str(datetime.datetime.now())[:10])
    def test_lineitem(self):
        order = Order.objects.get(id=1)
        lineitem = LineItem.objects.get(order=order)
        self.assertTrue(lineitem.created_date)
        self.assertEqual('2023-05-01', lineitem.product.booking_date)