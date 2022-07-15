from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout

from .models import *
from .forms import CreateUserForm


# Create your views here.

def registrationpage(request):
    form = CreateUserForm()
    print("Registration Page...")

    if request.method == 'POST':
        print("Form Submitted!")
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created for ' + user)
            return redirect('loginpg')

    context = {'form':form}
    return render(request, 'hosp/registrationpage.html', context)

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
 

        user = authenticate(request, username = username, password1 = password1)

        if user is not None: 
            login(request, username)
            redirect('index')

    context = {}
    return render(request, 'hosp/loginpage.html')

def index(request):
    return render(request, 'hosp/index.html')

