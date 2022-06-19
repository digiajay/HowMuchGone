from django.shortcuts import render

# Create your views here.
def index(request):
    '''Home page render'''
    return render(request,'index.html')

def expenses(request):
    '''Expenses history render'''
    return render(request,'expenses.html')

def add_expense(request):
    '''Add Expenses here'''
    return render(request, 'add_expense.html')