from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from django.core.cache import cache
from api.models import Wallets
from bit import Key


def logout_and_clear(request):
    logout(request)
    cache.clear()
    response = HttpResponseRedirect('/')
    for cookie in request.COOKIES:
        response.delete_cookie(cookie)
    return response

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

            # wallet configuration
            wallets = Wallets.objects

            try:
                wallet = wallets.get(user_id=request.user)
                print('já tem wallet')
            except:
                print('nao tem wallet')
                new_wallet = create_wallet()
                wallet = Wallets(
                    private_key = new_wallet['key'],
                    private_key_wif = new_wallet['key_wif'],
                    public_key_hex = new_wallet['pub_key_hex'],
                    address = new_wallet['pub_address'],
                    user = request.user
                )

                wallet.save()

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

#wallets
def create_wallet():
    key = Key()
    wif_key = key.to_wif()
    pub_key_hex = key.public_key.hex()
    pub_address = key.address

    return {
        "key": key,
        "key_wif": wif_key,
        "pub_key_hex": pub_key_hex,
        "pub_address": pub_address
    }
