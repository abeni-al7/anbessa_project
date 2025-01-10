# complaints/permissions.py
from rest_framework import permissions


class IsComplaintOwnerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow creation only if authenticated
        if request.method == "POST":
            return request.user.is_authenticated
        if request.method == "GET":
            return request.user.is_staff
        return True

    def has_object_permission(self, request, view, obj):
        # Allow PUT/PATCH/DELETE only if user is admin or owner
        if request.method in permissions.SAFE_METHODS:
            return True
        return (obj.user_id == request.user) or request.user.is_staff
