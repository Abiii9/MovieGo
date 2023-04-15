from django.contrib import admin
from .models import Votes, Languages, Countries, Companies, Movies
# Register your models here.
admin.site.register(Votes)
admin.site.register(Languages)
admin.site.register(Countries)
admin.site.register(Companies)
admin.site.register(Movies)