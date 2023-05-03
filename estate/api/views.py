from estate import models
from estate.api import serializers

from rest_framework.viewsets import ModelViewSet


class EstateViewSet(ModelViewSet):
    '''
    The Estate ViewSet class is for designing and managing and displaying Estate model.
    '''

    queryset = models.Estate.objects.all()
    serializer_class = serializers.EstateSerializer
    lookup_field = 'slug'