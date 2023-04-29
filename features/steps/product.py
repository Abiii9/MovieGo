import urllib
from urllib.parse import urljoin
from behave import given, when, then
from movie_go.models import Votes, Languages, Countries, Companies, Movies, Zones
from faker import Faker
@given("we want to add a product")
def user_on_product_newpage(context):
    fake = Faker()
    Votes.objects.create(vote_average= 6.7,vote_count = 89)
    vote_obj1 = Votes.objects.get(id=1)
    Languages.objects.create(spoken_languages="[{'iso_639_1': 'en', 'name': 'English'}]")
    lang_obj1 = Languages.objects.get(id=1)
    Countries.objects.create(production_countries="[{'iso_3166_1': 'US', 'name': 'United States of America'}]")
    country_obj1 = Countries.objects.get(id=1)
    Companies.objects.create(production_companies="[{'name': 'Pixar Animation Studios', 'id': 3}]")
    company_obj1 = Companies.objects.get(id=1)
    Movies.objects.create(belongs_to_collection="{'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}",budget=5000000,genres="[{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]",
    movie_id= 862, overview="Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.",
    popularity=21.946943, production_companies= company_obj1, production_countries= country_obj1,
    release_date= "30-10-1995",revenue=6000000,runtime = 135, spoken_languages= lang_obj1,
    tagline= " ",title="Toy Story", votes= vote_obj1,poster_path="/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg")
    Zones.objects.create(seats=5,screenwidth=40,aspect_ratio='16:9',resolution='2K',image='10_seater.jpg', address=fake.address(), cost= 80)
    base_url = urllib.request.url2pathname(context.test_case.live_server_url)
    print(base_url)
    open_url = urljoin(base_url,'product_new/1/1')
    context.browser.get(open_url)


@when(u'we fill in the form')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we fill in the form')


@then(u'it succeeds')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then it succeeds')


@given(u'we have specific products to add')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given we have specific products to add')


@when(u'we visit the listing page')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we visit the listing page')


@then(u'we will find \'another thing\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then we will find \'another thing\'')