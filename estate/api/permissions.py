from rest_framework.permissions import BasePermission



class IsOwner(BasePermission):
    """
    This class is for return owner object access.
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
