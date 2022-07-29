from django.shortcuts import render, redirect
from .models import Account
from .forms import ClientForm, DevForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout




# Client Register View

def Client_Register(request):
    form = ClientForm()

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            company_name = form.cleaned_data['company_name']
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user( full_name = full_name, company_name=company_name, email = email, username = username, password = password)
            user.save()
            return redirect('login')
    
    context = {
        'form' : form
    }

    return render(request, 'auth/register-client.html', context)

# Dev Register View

def Dev_Register(request):
    form = DevForm()
    
    if request.method == 'POST':
        form = DevForm(request.POST)
        if form.is_valid():
            company_name = form.cleaned_data['company_name']
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user( full_name = full_name, company_name=company_name, email = email, username = username, password = password)
            user.save()
            return redirect('login')
    
    context = {
        'form' : form
    }

    return render(request, 'auth/register-dev.html', context)


# Login View

def Login_View(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password'] 

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_manager:
                return redirect('index')                
            return redirect('index')
        else:
            messages.info(request, 'Username or Password is incorrect')
    return render(request, 'auth/login.html')


# Logout function

def Logout_View(request):
    logout(request)
    return redirect('login')




