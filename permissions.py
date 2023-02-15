from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    message = "access denied , you are not owener"

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user

    def has_object_permission(self, request, view, obj):
        if request.method == permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
