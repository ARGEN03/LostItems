from rest_framework import permissions


class ISstaff(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.is_staff
