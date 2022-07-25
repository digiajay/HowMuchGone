from tkinter import CASCADE
from django.db import models
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User

# Create your models here.

class Expense_Categories(models.Model):
    expense_type = models.CharField(max_length=25)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"{self.expense_type}"
        
class Expenses(models.Model):
    '''Adding model for daily expense tracker'''
    ''' A short description of the expense'''
    expense_short = models.CharField(max_length=50)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    ''' Expense value'''
    expense_value = MoneyField(max_digits=14, decimal_places=2, default_currency='EUR')
    #expense_value = models.FloatField()
    #expense_currency = models.DecimalField(max_digits=6,decimal_places=2)

    expense_date = models.DateField(auto_now=True)

    #expense_category = models.CharField(max_length=50)
    expense_category = models.ForeignKey(Expense_Categories, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"{self.expense_date}: {self.expense_value} - {self.expense_short} - {self.expense_category}" 
