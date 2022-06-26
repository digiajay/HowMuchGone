import django


from django import forms
from .models import Expense_Categories, Expenses

class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ['expense_short', 'expense_value', 'expense_category']
        labels = {
                    'Description':'Enter Short Description',
                    'Value':'Enter value of expenese',
                    'Category':'Enter expense category',
                }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Expense_Categories
        fields = ['expense_type']
        labels = {
                    'Category':'Add new category here'
                }