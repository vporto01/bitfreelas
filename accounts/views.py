from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .forms import CustomUserCreationForm

def login_view(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')
    else:
        email = request.POST.get('email')
        print(email)
        password = request.POST.get('password')
        print(password)
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('projects'))
        else:
            return HttpResponse('Credenciais inválidas')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})
