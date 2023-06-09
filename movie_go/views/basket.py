from decimal import Decimal
from django.conf import settings
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_POST
from movie_go.models import Product
from movie_go.forms import BasketAddProductForm 

#creating a Basket class and a few methods to manipulate the basket
class Basket(object):
    # a data transfer object to shift items from cart to page
    # inspired by Django 3 by Example (2020) by Antonio Mele
    # https://github.com/PacktPublishing/Django-3-by-Example/
    
    #creating an initial version of a basket
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if not basket:
            # save an empty basket in the session
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket
    #to iterate over the items in the basket and fetch the corresponding product from database.
    def __iter__(self):
        product_ids = self.basket.keys()
        # get the product objects and add them to the basket
        products = Product.objects.filter(id__in=product_ids)

        basket = self.basket.copy()
        for product in products:
            basket[str(product.id)]['product'] = product
            basket[str(product.id)]['product_id'] = product.id

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    #to return the number of items in the basket.
    def __len__(self):
        return sum(item['quantity'] for item in self.basket.values())
    #Add a product to the basket or update its quantity.
    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.basket:
            self.basket[product_id] = {'quantity': 0,
                                      'price': str(product.price)}
        if override_quantity:
            self.basket[product_id]['quantity'] = quantity
        else:
            self.basket[product_id]['quantity'] += quantity
        self.save()

    # mark the session as "modified" to make sure it gets saved
    def save(self):
        self.session.modified = True

    #to remove a particular product from basket
    def remove(self, product):
        """
        Remove a product from the basket.
        """
        product_id = str(product.id)
        if product_id in self.basket:
            del self.basket[product_id]
            self.save()
    #to clear the basket session
    def clear(self):
        # remove basket from session
        del self.session[settings.BASKET_SESSION_ID]
        self.save()
    #to get the total price from the basket contents
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.basket.values())

#allows user to add products to the basket, and view the contents in the basket once the 
#product has been added.
@require_POST
def basket_add(request, product_id):
    try:
        basket = Basket(request)
        product = get_object_or_404(Product, id=product_id)
        form = BasketAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            basket.add(product=product,quantity=cd['quantity'],override_quantity=cd['override'])
        return redirect('movie_go:basket_detail')
    except:
        return render(request, 'movie_go/500.html')

#allows user to remove products from the basket, and view the contents in the basket once the 
#product has been removed.
@require_POST
def basket_remove(request, product_id):
    try:
        if product_id != 0:
            basket = Basket(request)
            product = get_object_or_404(Product, id=product_id)
            basket.remove(product)
            return redirect('movie_go:basket_detail')
        else:
            return redirect('movie_go:movies')
    except:
        return render(request, 'movie_go/500.html')

#allows the user to veiw contents of the basket.
def basket_detail(request):
    try:
        basket = Basket(request)
        for item in basket:
            item['update_quantity_form'] = BasketAddProductForm(initial={'quantity': item['quantity'],'override': True})
        return render(request, 'movie_go/basket.html', {'basket': basket})
    except:
        return render(request, 'movie_go/500.html')