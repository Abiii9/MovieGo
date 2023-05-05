from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from movie_go.models import LineItem, Order, Customer
from django.contrib.auth.decorators import login_required

#allows the users to view teh list of orders they have made.
@login_required(login_url='movie_go:login')
def user_order_list(request):
    try:
        user = request.user
        customer = get_object_or_404(Customer, user_id=user.id)
        orders = Order.objects.filter(customer=customer)
        return render(request, 'movie_go/order_list.html', {'orders': orders, 'user': user})
    except:
        return render(request, 'movie_go/500.html')

#allows the user to view the details of a particular order.
@login_required(login_url='movie_go:login')
def user_order_detail(request, id):
    try:
        order = get_object_or_404(Order, id=id)
        customer = order.customer
        user = get_object_or_404(User, id=customer.pk)
        line_items = LineItem.objects.filter(order_id=order.id)
        return render(request, 'movie_go/order_detail.html', {'order' : order, 'user': user, 'line_items': line_items})
    except:
        return render(request, 'movie_go/500.html')