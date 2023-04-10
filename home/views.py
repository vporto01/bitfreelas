from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.urls import reverse

def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('projects'))
    return render(request, r'home\home.html')
