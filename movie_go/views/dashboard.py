from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from movie_go.models import Zones, Movies, Customer, Order, Product, Cart, LineItem
from datetime import datetime
from collections import Counter
from django.core.exceptions import PermissionDenied
def chart_data(Model):
    op = []
    total_data = Model.objects.values_list('created_date').order_by('-created_date')
    for date in total_data:
        op.append(str(date[0])[:10])
    return dict(Counter(op))

def data_count(Model):
    data = Model.objects.count()
    return data

def data_today(Model):
    current = str(datetime.now())[:10]
    data = Model.objects.filter(created_date__contains=current).count()
    return data
@login_required
def dashboard(request):
    user = request.user
    if user.is_authenticated & user.is_staff:
        #chart processsing
        order_data = chart_data(Order)
        x1Values = order_data.keys()
        y1Values = order_data.values()
        listx1 = list(x1Values)
        listx1.reverse()
        listy1 = list(y1Values)
        listy1.reverse()
        customer_data = chart_data(Customer)
        x2Values = customer_data.keys()
        y2Values = customer_data.values()
        listx2 = list(x2Values)
        listx2.reverse()
        listy2 = list(y2Values)
        listy2.reverse()
        #count_processing
        order_count = data_count(Order)
        customers_count = data_count(Customer)
        #count today
        orders_today = data_today(Order)
        print(orders_today)
        customers_today = data_today(Customer)
        return render(request, 'movie_go/dashboard.html',{'x1Values': listx1,'y1Values': listy1,'x2Values': listx2,'y2Values': listy2, 'order_count': order_count, 'customers_count': customers_count, 'orders_today': orders_today, 'customers_today': customers_today})
    elif not user.is_staff & user.is_authenticated:
        raise PermissionDenied()
    else:
        return redirect('movie_go:login')