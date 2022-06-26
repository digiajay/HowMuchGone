from unicodedata import name
from django.urls import path
from . import views

app_name = 'hmg'

urlpatterns = [
    path('', views.index, name='index'),

    #'''List all Expense Categories'''
    path('expense_categories',views.expense_categories,name='expense_categories'),

    #'''Expenses history'''
    path('expenses',views.expenses,name='expenses'),

    #'''Add New Expense'''
    path('add_expense',views.add_expense,name='add_expense'),

    #'''Add New Category'''
    path('add_category',views.add_expense_category,name='add_expense_category')    

]
