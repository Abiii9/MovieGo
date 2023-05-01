import urllib
from urllib.parse import urljoin
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User
from behave import given, when, then
from movie_go.models import Votes, Languages, Countries, Companies, Movies, Zones, Product, Order, Customer, LineItem, Cart
from faker import Faker
from behave import fixture, use_fixture
from faker import Faker

@fixture
def setup_model_objects(context):
    fake = Faker()
    # Create model objects
    Votes.objects.create(vote_average= 6.7,vote_count = 89)
    vote_obj1 = Votes.objects.get(id=1)
    Languages.objects.create(spoken_languages="[{'iso_639_1': 'en', 'name': 'English'}]")
    lang_obj1 = Languages.objects.get(id=1)
    Countries.objects.create(production_countries="[{'iso_3166_1': 'US', 'name': 'United States of America'}]")
    country_obj1 = Countries.objects.get(id=1)
    Companies.objects.create(production_companies="[{'name': 'Pixar Animation Studios', 'id': 3}]")
    company_obj1 = Companies.objects.get(id=1)
    movie1 = Movies.objects.create(belongs_to_collection="{'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}",budget=5000000,genres="[{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]",
    movie_id= 862, overview="Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.",
    popularity=21.946943, production_companies= company_obj1, production_countries= country_obj1,
    release_date= "30-10-1995",revenue=6000000,runtime = 135, spoken_languages= lang_obj1,
    tagline= " ",title="Toy Story", votes= vote_obj1,poster_path="/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg")
    zone1 = Zones.objects.create(seats=5,screenwidth=40,aspect_ratio='16:9',resolution='2K',image='10_seater.jpg', address=fake.address(), cost= 80)
    zone2 = Zones.objects.create(seats=5,screenwidth=40,aspect_ratio='16:9',resolution='2K',image='10_seater.jpg', address=fake.address(), cost= 60)
    product1 = Product.objects.create(movie=movie1, zone=zone1, booking_date='2023-09-07', booking_time='13:01', price=7+zone1.cost)
    user1 = User.objects.create_user(username = 'JohnAbraham',first_name = 'John',last_name = 'Abraham',email = 'john.abraham@somemail.com', password = 'p@ssw0rd')
    customer1 = Customer.objects.get(user=user1)
    customer1.address='123, Dubai Main Road, Dubai'
    customer1.save()
    order1 = Order.objects.create(customer=customer1)
    cart1 = Cart.objects.create(product=product1,quantity=1)
    lineitem1 = LineItem.objects.create(quantity=3,product=product1,cart=cart1,order=order1)
    # Store the model objects in the context
    context.vote_obj1 = vote_obj1
    context.lang_obj1 = lang_obj1
    context.country_obj1 = country_obj1
    context.company_obj1 = company_obj1
    context.movie1 = movie1
    context.zone1 = zone1
    context.zone2 = zone2
    context.product1 = product1

    yield

    #clean up the model objects after the scenario finishes
    vote_obj1.delete()
    lang_obj1.delete()
    country_obj1.delete()
    company_obj1.delete()
    movie1.delete()
    zone1.delete()
    zone2.delete()
    product1.delete()
    user1.delete()
    customer1.delete()
    order1.delete()
    cart1.delete()
    lineitem1.delete()


@given(u'user is on the homepage for logout and already logged in')
def step_impl(context):
    use_fixture(setup_model_objects, context)
    base_url = urllib.request.url2pathname(context.test_case.live_server_url)
    open_url = urljoin(base_url,'/')
    context.browser.get(open_url)
    context.browser.find_element(By.CLASS_NAME, "login_btn").click()
    usernamefield = context.browser.find_element('name','username')
    usernamefield.send_keys('JohnAbraham')
    passwordfield = context.browser.find_element('name','password')
    passwordfield.send_keys('p@ssw0rd')
    context.browser.find_element('name','Login').click()

@when(u'user clicks on the logout button')
def step_impl(context):
    context.browser.find_element(By.CLASS_NAME,'logout_btn').click()

@then(u'user is able to log out of the application')
def step_impl(context):
    assert 'Welcome' not in context.browser.page_source