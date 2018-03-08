from rest_framework.permissions import BasePermission


class IsTopicOwner(BasePermission):

    message = "You don't have access to this topic"

    def has_permission(self, request, view, obj):
        return request.user == obj.user
