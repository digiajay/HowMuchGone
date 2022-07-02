""" Define URL patterns for users """

from django.urls import path, include

from django.contrib.auth import urls as usersAuthUrls

from . import views

app_name = 'users'

urlpatterns = [
    #include default auth url
    path('', include(usersAuthUrls)),
    path('register', views.register, name='register')
]
