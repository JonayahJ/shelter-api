# Shelters URLs
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('shelters', views.ShelterView) # How to access online

urlpatterns = [
    path('', include(router.urls))
]