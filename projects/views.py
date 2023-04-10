from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from api.models import Client, Freelancer
from projects.models import Projects

def get_user_type(user):
    is_client = Client.objects.filter(user=user).exists()
    is_freelancer = Freelancer.objects.filter(user=user).exists()

    if is_client:
        return 'client'
    elif is_freelancer:
        return 'freelancer'
    else:
        return 'unknown'

@login_required(login_url='/accounts/login/')
def projects_view(request):
    if request.method == 'GET':

        user_type = get_user_type(request.user)

        context = {
            "user_type": user_type
        }

        if user_type == "client":

            client_profile = Client.objects.get(user_id=request.user.id)

            if client_profile.avatar:
                profile_picture_url = client_profile.avatar.url
            else:
                profile_picture_url = None

            context['profile_picture_url'] = profile_picture_url


            user_logged_name = request.user
            context['user_logged'] = user_logged_name

            list_quantity = 3
            freelancers = Freelancer.objects.all()[0 : list_quantity]

            context["freelancers"] = freelancers
            context["top_freelancers_quantity"] = list_quantity

            projects = Projects.objects.all()

            context['projects'] = projects

            return render(request, template_name=r'projects\logged_homepage\clients\index.html', context=context)

        elif user_type == "freelancer":

            client_profile = Freelancer.objects.get(user_id=request.user.id)

            if client_profile.avatar:
                profile_picture_url = client_profile.avatar.url
            else:
                profile_picture_url = None

            context['profile_picture_url'] = profile_picture_url

            projects = Projects.objects.all()

            context['projects'] = projects

            return render(request, template_name=r'projects\logged_homepage\freelancers\index.html', context=context)
        
        else:
            return redirect('/admin')

# def chat_room(request, room_name):
#     return render(request, r'projects\logged_homepage\chat\chat_room.html', {'room_name': room_name})

