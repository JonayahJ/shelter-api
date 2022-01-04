from django.shortcuts import render
from rest_framework import viewsets
from .models import Shelter
from .serializers import ShelterSerializer

# Shelter View
class ShelterView(viewsets.ModelViewSet):
    queryset = Shelter.objects.all() # All the objects in the model
    serializer_class = ShelterSerializer # JSON converter

    