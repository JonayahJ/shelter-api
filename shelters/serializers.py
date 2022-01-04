from rest_framework import serializers
from .models import Shelter

class ShelterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shelter
        fields = (
            'id',
            'url',
            'name',
            'street_address',
            'city',
            'state',
            'zip',
            'telephone',
            'type_of_shelter',
            'shelter_services'
        )