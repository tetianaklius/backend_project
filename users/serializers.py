from django.contrib.auth import get_user_model
from django.db.transaction import atomic
from rest_framework import serializers

from core.services.email_service import EmailService
from users.models import ProfileModel, ProfileStaffModel

UserModel = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ("id",
                  "name",
                  "surname",
                  "age",
                  "created_at",
                  "updated_at",
                  )


class StaffProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileStaffModel
        fields = ("id",
                  "name",
                  "surname",
                  "age",
                  "city",
                  "experience",
                  "phone",
                  "public_email",
                  "created_at",
                  "updated_at",
                  "user"
                  )


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = (
            "id",
            "email",
            "password",
            "is_active",
            "is_staff",
            "is_main_manager",
            "is_superuser",
            "last_login",
            "created_at",
            "updated_at",
            "profile"
        )
        read_only_fields = (
            "id", "is_active", "is_main_manager", "is_staff", "is_superuser", "last_login", "created_at", "updated_at")
        extra_kwargs = {
            "password": {
                "write_only": True,
            }
        }

    @atomic
    def create(self, validated_data: dict):
        profile = validated_data.pop("profile")
        user = UserModel.objects.create_user(**validated_data)
        # if not user.is_staff:
        ProfileModel.objects.create(**profile, user=user)
        # else:
        #     ProfileStaffModel.objects.create(**profile)

        EmailService.register_email(user)
        return user


class StaffUserSerializer(serializers.ModelSerializer):
    staff_profile = StaffProfileSerializer()

    class Meta:
        model = UserModel
        fields = ("id", "staff_profile")

    @atomic
    def patch(self, validated_data: dict):
        profile = validated_data.pop("staff_profile")
        user = UserModel.objects.get(id=validated_data["id"])
        if user.is_staff:
            ProfileStaffModel.objects.create(**profile, user=user)
        return user



# class StaffUserSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = UserModel
#         fields = (
#             "id",
#             "email",
#             "password",
#             "is_active",
#             "is_staff",
#             "is_main_manager",
#             "is_superuser",
#             "last_login",
#             "created_at",
#             "updated_at",
#             "staff_profile"
#         )
#         read_only_fields = (
#             "id", "is_active", "is_main_manager", "is_superuser", "last_login", "created_at", "updated_at")
#         extra_kwargs = {
#             'password': {
#                 'write_only': True,
#             }
#         }
#
#     @atomic
#     def create(self, validated_data: dict):
#         profile = validated_data.pop("staff_profile")
#         user = UserModel.objects.create_user(**validated_data)
#         ProfileStaffModel.objects.create(**profile, user=user)
#         EmailService.register_email(user)
#         return user


