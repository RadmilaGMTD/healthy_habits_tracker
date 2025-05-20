from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True


class IsPublicOrIsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.is_public or obj.user == request.user:
            return True
