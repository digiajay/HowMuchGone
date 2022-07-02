from django.shortcuts import redirect, render

from .forms import ExpensesForm, CategoryForm


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
    if request.method != 'POST':
        form = ExpensesForm()
    else:
        form = ExpensesForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_traces:expenses')
    context = {'form':form}
    return render(request, 'add_expense.html', context)

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