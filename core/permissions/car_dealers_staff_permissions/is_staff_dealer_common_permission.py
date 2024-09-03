from django.contrib.auth import get_user_model

from rest_framework.permissions import BasePermission

from core.dataclasses.user_dataclass import User

UserModel: User = get_user_model()


class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)
