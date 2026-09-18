"""
URL configuration for hmsbackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from hmsbackend.accounts.views import signup, login
from hmsbackend.bookings.views import create_slot, get_slots, book_slot
from . import views

urlpatterns = [
   path('', views.home),
   path('admin/', admin.site.urls),
   path('signup/', signup),
   path('login/', login),
   path('create-slot/', create_slot),
   path('get-slot/', get_slots),
   path('book-slot/', book_slot),
   path('home/', views.home, name="home"),
    
]
