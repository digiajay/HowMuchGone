from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.
class Expenses(models.Model):
    '''Adding model for daily expense tracker'''
    ''' A short description of the expense'''
    expense_short = models.CharField(max_length=50)

    ''' Expense value'''
    expense_value = MoneyField(max_digits=14, decimal_places=2, default_currency='EUR')
    #expense_value = models.FloatField()
    #expense_currency = models.DecimalField(max_digits=6,decimal_places=2)

    timestamp_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.expense_currency} {self.expense_value} - {self.expense_short}" 

class Expense_Categories(models.Model):
    expense_type = models.CharField(max_length=25)
    
    def __str__(self) -> str:
        return f"{self.expense_type}"