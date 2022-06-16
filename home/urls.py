from django.contrib import admin
from django.urls import path
from home import views

app_name='Veggie'

urlpatterns = [
     path("",views.login, name='login'),
      path("login",views.login, name='login'),
    path("index",views.index, name='index'),
    path("about",views.about, name='about'),
    path("service",views.service, name='service'),
    path("contact",views.contact, name='contact'),
    path("help",views.help, name='help'),
    path("register",views.register,name='register')
        
]