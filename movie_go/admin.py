from django.contrib import admin
from .models import Votes, Languages, Countries, Companies, Movies, Zones, Cart, Customer, LineItem, Order, Product
# Register your models here.
admin.site.register(Votes)
admin.site.register(Languages)
admin.site.register(Countries)
admin.site.register(Companies)
admin.site.register(Movies)
admin.site.register(Zones)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(LineItem)
admin.site.register(Order)
admin.site.register(Product)