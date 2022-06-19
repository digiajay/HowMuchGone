from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    #'''Expenses history'''
    path('expenses',views.expenses,name='expenses'),

    #'''Add New Expense'''
    path('add_expense',views.add_expense,name='add_expense'),

]
