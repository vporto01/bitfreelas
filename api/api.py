from rest_framework import viewsets
from .models import Client, Freelancer
from .serializers import ClientSerializer, FreelancerSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class FreelancerViewSet(viewsets.ModelViewSet):
    queryset = Freelancer.objects.all()
    serializer_class = FreelancerSerializer
