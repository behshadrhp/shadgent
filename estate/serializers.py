from rest_framework import serializers
from estate import models


class EstateSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(read_only=True)

    def create(self, validated_data):
        owner = self.context['owner']
        return models.Estate.objects.create(owner=owner, **validated_data)

    class Meta:
        model = models.Estate
        fields = [
            'owner',
            'title',
            'slug',
            'description',
            'address',
            'status_estate',
            'type_of_property_estate',
            'type_of_estate_request',
            'meterage',
            'number_room',
            'number_of_floors',
            'year_made',
            'elevator',
            'parking',
            'yard',
        ]
