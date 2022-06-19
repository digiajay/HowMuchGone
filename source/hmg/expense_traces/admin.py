from django.contrib import admin

# Register your models here.
from .models import Expense_Categories,Expenses

admin.site.register(Expense_Categories)
admin.site.register(Expenses)