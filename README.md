# MovieGo v1.0 05-05-2023

## What is it

This application has been developed as a part of an assignment of the Enterprise Software Development course. This is an e-commerce application that allows people to enjoy theatre-like experience along with their friends at a reasonable price . There is a collection of more than four thousand movies along with five mini-theatre zones for the users to pick. The dataset for the movies has been taken from Kaggle.(https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?select=movies_metadata.csv).


## Where to get it

The source code is hosted on Render at https://moviego-k3mo.onrender.com/

## How to install and begin running the application

To get MovieGo up and running, the following steps need to be followed.

~~~
pyenv install 3.11.0
pyenv local 3.11.0
py -3 -m venv .venv
source  venv/bin/activate
pip install --upgrade pip
pip install Django
~~~

## Technologies used

- HTML
- CSS
- Python Django
- JavaScript
- Gherkin

There are some libraries that have been used in this project. 

This includes Behave, Selenium and Webdriver-manager for Behavioral Driven Development Testing.
Chart.js - this is a JavaScript library that has been used to render the charts for the dashboard page.


The following dependencies need to be installed.
~~~
pip install selenium
pip install behave
pip install webdriver-manager
pip install gunicorn
~~~
Instead, run the following command to get all the dependencies installed at once.

~~~
pip install -r raquirements.txt
~~~
Now, run the following command to start the development server.

~~~
python3 manage.py runserver 0.0.0.0:8000
~~~

## How to use it

Here are a few features that assist to navigate the application effectively.

- The index page consists of a general overview of the application along with the options to view the zones and movies.
- The about page that gives a detailed overview of the application.
- The movies page that lists a collection of top-rated movies. You can search for a specific movie with the help of a movie search bar, along with various genres that present the top-rated movies in them.
- The movie details page list out specific information about a movie such as the average votes, the languages in which it has been produced, the overview of the movie's storyline etc.
- The zones page give out the details about the zones in which the users can watch a selected movie.
- The ability to add a movie and a zone as a product and add them to the basket.
- The selected product can be edited or removed from the basket.
- Ability to purchase the order by entering credit card details.
- A sophisticated authentication system for secure user account maintenance.
- A dashboard for staff users that can view the charts for orders and customer count per day.
- An order list page that enables users to view a list and in-detail view of the orders they have made.

## Maintenance

Please make sure that you have installed the latest version of the dependencies.

## User account details

superuser
username: admin
password: moviego@123

staff user
username: SarahWalter
password: p@ssw0rd

customer user
username: JasmineOdom
password: p@ssw0rd


## Credits
The dataset has been taken from Kaggle (https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?select=movies_metadata.csv).
The images for the movies have been fetched from the TMDB API (https://www.themoviedb.org/documentation/api)
