from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
def projects_view(request):
    if request.method == 'GET':
        # return render(request, 'accounts/login.html')

        return render(request, template_name=r'projects\index.html')

