from rest_framework.viewsets import ModelViewSet
from estate import models, serializers


class EstateViewSet(ModelViewSet):
    '''EstateViewSet is a kind of class for presenting the real estate model,
      as an api with rest-framework.'''

    queryset = models.Estate.objects.all()
    serializer_class = serializers.EstateSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    lookup_field = 'slug'

    def get_serializer_context(self):
        owner = self.request.user
        return {'owner': owner}
