from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from accounts.forms import RegisterForm


# Create your views here.

def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('common:home')

    else:
        form = AuthenticationForm()

    return render(request, 'accounts/sign_in.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('common:home')

    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html')

def sign_out(request):
    logout(request)
    return redirect('common:home')