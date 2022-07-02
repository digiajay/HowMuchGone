import imp
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.

def register(request):
    """Registering a new user"""
    if request.method != 'POST':
        """Provide user creation form"""
        form = UserCreationForm()
    else:
        """Process the registration form"""
        form = UserCreationForm(data=request.POST)

        if (form.is_valid):
            new_user = form.save()
            #Login the user and redirect
            login(request, new_user)
            return redirect('expense_traces:index')

    #Display blank form for user creation
    context = {'form': form}
    return render(request,'registration/registration.html',context)