from django.urls import path
from rest_framework.routers import DefaultRouter
from .api import ClientViewSet, FreelancerViewSet
from . import views  # Adicione esta linha

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'freelancers', FreelancerViewSet, basename='freelancer')

# Adicione as rotas de autenticação abaixo das rotas geradas pelo router
urlpatterns = [
    path('register/', views.register, name='api_register'),
    # ... (adicione outras rotas relacionadas à autenticação, como login e logout)
] + router.urls
