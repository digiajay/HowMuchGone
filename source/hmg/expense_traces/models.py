from django.db import models

# Create your models here.
class Daily_Expense(models.Model):
    '''Adding model for daily expense tracker'''
    ''' A short description of the expense'''
    expense_short = models.CharField(max_length=50)

    ''' Expense value'''
    expense_value = models.FloatField()

    expense_currency = models.CharField(max_length=1)

    timestamp_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.expense_currency} {self.expense_value} - {self.expense_short}" 