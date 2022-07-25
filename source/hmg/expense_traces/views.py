from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import ExpensesForm, CategoryForm


from .models import Expenses, Expense_Categories
# Create your views here.
def index(request):
    '''Home page render'''
    return render(request,'index.html')

@login_required
def expense_categories(request):
    '''List all expense categories here render'''
    expense_categories = Expense_Categories.objects.filter(owner=request.user).order_by('id')
    context = {'categories':expense_categories}
    return render(request,'expense_categories.html',context)

@login_required
def expenses(request):
    '''Render all expenses'''
    expenses = Expenses.objects.filter(owner=request.user).order_by('expense_date')
    context = {'expenses': expenses}
    return render(request, 'expenses.html', context)

@login_required
def add_expense(request):
    '''Add Expenses here'''
    if request.method != 'POST':
        form = ExpensesForm()
    else:
        form = ExpensesForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_traces:expenses')
    context = {'form':form}
    return render(request, 'add_expense.html', context)

@login_required
def add_expense_category(request):
    '''Add categories here'''
    if request.method != 'POST':
        form = CategoryForm()
    else:
        form = CategoryForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_traces:expense_categories')
    context = {'form':form}
    return render(request,'add_categories.html',context)