from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from api.models import Client, Freelancer, Wallets
from projects.models import Projects
import requests

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

def get_btc_usd_price():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        btc_usd_price = data['bitcoin']['usd']
        return btc_usd_price
    

def balance(request):

    address = Wallets.objects.get(user_id=request.user.id).address

    balance_sats = requests.get(f'https://api.blockchain.info/haskoin-store/btc/address/{address}/balance').json()['confirmed']


    context = {
        "balance_sats": balance_sats,
        "balance_btc": balance_sats/100000000,
        "balance_usd": f"{(balance_sats/100000000) * get_btc_usd_price():.2f}"
    }

    return render(request, template_name=r'projects\logged_homepage\clients\balance.html', context=context)
