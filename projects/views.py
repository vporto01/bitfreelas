from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Client, Freelancer

def get_user_type(user):
    is_client = Client.objects.filter(user=user).exists()
    is_freelancer = Freelancer.objects.filter(user=user).exists()

    if is_client:
        return 'client'
    elif is_freelancer:
        return 'freelancer'
    else:
        return 'unknown'

@login_required(login_url='login')
def projects_view(request):
    if request.method == 'GET':
        # Imprime o nome de usuário do usuário logado no console
        print("Usuário logado:", request.user.username)

        user_type = get_user_type(request.user)
        print(f'{request.user.username} is a {user_type}')
        
        return render(request, template_name=r'projects\index.html')

