from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from movie_go.forms import BasketAddProductForm, ProductForm
from movie_go.models import Product, Movies, Zones
#list the total products present
def product_list(request):
    try:
        products = Product.objects.all()    
        return render(request, 'movie_go/product_list.html', {'products' : products })
    except:
        return render(request, 'movie_go/500.html')

#allows the user to view the in-detail information about the selected product.
def product_detail(request, id=None):
    try:
        if id:
            product = get_object_or_404(Product, id=id)
        else:
            product = None
        basket_product_form = BasketAddProductForm()
        return render(request, 'movie_go/product_detail.html', {'product' : product, 'basket_product_form': basket_product_form })
    except:
        return render(request, 'movie_go/500.html')

#allows the user to add a new product
def product_new(request,movie_id,zone_id):
    try:
        movie = Movies.objects.get(id=movie_id)
        zone = Zones.objects.get(id=zone_id)
        if request.method=="POST":
            form = ProductForm(request.POST)
            if form.is_valid():
                product = form.save(commit=False)
                product.price = float(7+zone.cost)        
                product.created_date = timezone.now()
                product.save()
                return redirect('movie_go:product_detail', id=product.id)
        else:
            form = ProductForm(initial={'movie': movie.id,'zone': zone.id})
        return render(request, 'movie_go/product_edit.html', {'form': form, 'movie': movie})
    except:
        return render(request, 'movie_go/500.html')

#allows the user to edit an already created product.
def product_edit(request, id):
    try:
        product = get_object_or_404(Product, id=id)
        if request.method=="POST":
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                product = form.save(commit=False)
                product.created_date = timezone.now()
                product.save()
                return redirect('movie_go:product_detail', id=product.id)
        else:
            form = ProductForm(instance=product)
        return render(request, 'movie_go/product_edit.html', {'form': form})
    except:
        return render(request, 'movie_go/500.html')

#allows the user to delete a product.
def product_delete(request, id):
    try:
        product = get_object_or_404(Product, id=id)
        deleted = request.session.get('deleted', 'empty')
        request.session['deleted'] = product.id
        product.delete()
        return redirect('movie_go:movies')
    except:
        return render(request, 'movie_go/500.html')