from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, r'home\home.html')
