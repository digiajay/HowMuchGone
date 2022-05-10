from django.shortcuts import render

# Create your views here.
def index(request):
    '''Home page render'''
    return render(request,'index.html')