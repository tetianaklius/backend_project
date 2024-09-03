from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from users.serializers import UserSerializer, StaffUserSerializer
from core.permissions.platform_main_permissions.is_main_manager_permission import IsMainManager
from core.permissions.platform_main_permissions.is_superuser_permission import IsSuperUser
from core.permissions.car_dealers_staff_permissions.is_car_admin_permission import IsCarAdmin
from core.permissions.car_dealers_staff_permissions.is_car_manager_permission import IsCarManager

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class UserToMainManagerView(GenericAPIView):
    permission_classes = (IsSuperUser,)
    serializer_class = UserSerializer

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()

        user.is_main_manager = True
        user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserToStaffView(GenericAPIView):
    permission_classes = (IsSuperUser, IsMainManager, IsCarAdmin, IsCarManager)
    serializer_class = StaffUserSerializer

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()

        user.is_staff = True
        user.save()

        serializer = StaffUserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserBlockView(GenericAPIView):
    permission_classes = (IsSuperUser, IsMainManager,)
    serializer_class = UserSerializer

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()

        if user.is_active:
            user.is_active = False
            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserUnBlockView(GenericAPIView):
    permission_classes = (IsSuperUser, IsMainManager,)
    serializer_class = UserSerializer

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()

        if not user.is_active:
            user.is_active = True
            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)
