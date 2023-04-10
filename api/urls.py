from django.urls import path
from rest_framework.routers import DefaultRouter
from .api import ClientViewSet, FreelancerViewSet
from . import views 

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'freelancers', FreelancerViewSet, basename='freelancer')

urlpatterns = [
    path('register/', views.register, name='api_register'),
] + router.urls
