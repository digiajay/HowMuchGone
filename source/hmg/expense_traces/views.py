from django.shortcuts import render


from .models import Expenses, Expense_Categories
# Create your views here.
def index(request):
    '''Home page render'''
    return render(request,'index.html')

def expense_categories(request):
    '''List all expense categories here render'''
    expense_categories = Expense_Categories.objects.order_by('id')
    context = {'categories':expense_categories}
    return render(request,'expense_categories.html',context)

def expenses(request):
    '''Render all expenses'''
    expenses = Expenses.objects.order_by('expense_date')
    context = {'expenses': expenses}
    return render(request, 'expenses.html', context)

def add_expense(request):
    '''Add Expenses here'''
    return render(request, 'add_expense.html')