from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .forms import CustomUserCreationForm

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('projects'))

    if request.method == 'GET':
        return render(request, 'accounts/login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('projects'))
        else:
            error_message = 'Credenciais inválidas'
            return render(request, 'accounts/login.html', {'error_message': error_message})

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('projects'))
        
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})
