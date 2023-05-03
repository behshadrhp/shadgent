from estate import models

from rest_framework import serializers


class EstateSerializer(serializers.ModelSerializer):
    '''
    EstateSerializer class is for sending requests and displaying them public.
    '''

    owner = serializers.CharField(read_only=True)

    class Meta:
        model = models.Estate
        fields = [
            'owner',
            'title',
            'slug',
            'description',
            'address',
            'year_made',
            'status_estate',
            'type_of_property_estate',
            'type_of_estate_request',
            'meterage',
            'number_room',
            'number_of_floors',
            'elevator',
            'parking',
            'yard'
        ]
