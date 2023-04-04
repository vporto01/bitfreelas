from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects_view, name='projects'),
    # path('register/', views.register, name='register'),
]
