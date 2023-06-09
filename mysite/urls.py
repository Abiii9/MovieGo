"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movie_go.urls',  namespace='movie_go')),
]

#handling the 404 error, calling the corresponding view function incase of error.
handler404 = 'movie_go.views.basic.error_404_view'
#handling the 500 error, calling the corresponding view function incase of error.
handler500 = 'movie_go.views.basic.error_500_view'
#handling the 403 error, calling the corresponding view function incase of error.
handler403 = 'movie_go.views.basic.error_403_view'