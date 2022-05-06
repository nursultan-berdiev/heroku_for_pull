from rest_framework import permissions


class ItemPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method not in permissions.SAFE_METHODS:
            return bool(request.user and request.user.is_staff)
        else:
            return True

    def has_permission(self, request, view):
        if request.method not in permissions.SAFE_METHODS:
            return bool(request.user and request.user.is_staff)
        else:
            return True
