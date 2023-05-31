from estate import models
from estate.api import serializers

from rest_framework.viewsets import ModelViewSet

from .permissions import IsOwner


class EstateViewSet(ModelViewSet):
    '''
    The Estate ViewSet class is for designing and managing and displaying Estate model.
    '''

    queryset = models.Estate.objects.all()
    serializer_class = serializers.EstateSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)