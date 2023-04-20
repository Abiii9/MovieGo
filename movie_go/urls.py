from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movies, name='movies'),
    path('movies/<str:genre>', views.movies, name='movies'),
    path('product_details/<int:id>', views.product_details, name='product_details'),
]
