from django.contrib import admin
from django.urls import path,include
from . import views
from movie_go.views import basic, products, basket, orders
app_name = 'movie_go'
urlpatterns = [
    path('', views.basic.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('movies/', views.basic.movies, name='movies'),
    path('movies/<str:genre>', views.basic.movies, name='movies'),
    path('movie_details/<int:id>', views.basic.movie_details, name='movie_details'),
    path('zone_detail/<int:movie_id>', views.basic.zone_detail, name= 'zone_detail'),
    path('basket_add/<int:product_id>/', views.basket.basket_add, name ='basket_add'),
    path('basket_remove/<int:product_id>/', views.basket.basket_remove, name ='basket_remove'),
    path('basket_detail/', views.basket.basket_detail, name ='basket_detail'),
    path('product_list/', views.products.product_list, name='product_list'),
    path('product/<int:id>/', views.products.product_detail, name='product_detail'),
    path('product_new/<int:movie_id>/<int:zone_id>', views.products.product_new, name= 'product_new'),
    path('product_new/', views.products.product_new, name= 'product_new'),
    path('product/<int:id>/edit/', views.products.product_edit, name= 'product_edit'),
    path('product/<int:id>/delete/', views.products.product_delete, name= 'product_delete'),
    path('purchase/', views.basic.purchase, name ='purchase'),
    path('payment/', views.basic.payment, name ='payment'),
    path('signup/', views.basic.signup, name='signup'),
    path('user_order_list/', views.orders.user_order_list, name='user_order_list'),
    path('user_order/<int:id>/', views.orders.user_order_detail, name= 'user_order_detail'),
    path('dashboard/', views.basic.dashboard, name='dashboard'),
]
