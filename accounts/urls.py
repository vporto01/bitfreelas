from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_and_clear, name='logout'),

    # path('confirm-email/<uuid:confirmation_token>/', views.confirm_email, name='confirm_email'),
]
