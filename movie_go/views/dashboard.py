from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from movie_go.models import Zones, Movies, Customer, Order, Product, Cart, LineItem
from collections import Counter
def chart_data():
    op = []
    total_orders = Order.objects.values_list('created_date')
    for date in total_orders:
        op.append(str(date[0])[:10])
    return dict(Counter(op))

@login_required
def dashboard(request):
    user = request.user
    if user.is_authenticated & user.is_staff:
        data = chart_data()
        xValues = data.keys()
        yValues = data.values()
        listx = list(xValues)
        listx.reverse()
        listy = list(yValues)
        listy.reverse()
        print(listx)
        return render(request, 'movie_go/dashboard.html',{'xValues': listx,'yValues': listy})
    else:
        return redirect('movie_go:login')