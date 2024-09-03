from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.core import validators as v

from core.models import BaseModel
from dealerships.choises.staff_type_choice import StaffTypeChoices
from users.managers import UserManager


class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = "auth_user"
        ordering = ["id"]

    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_main_manager = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = "email"

    objects = UserManager()


class ProfileModel(BaseModel):
    class Meta:
        db_table = "profile"
        ordering = ["id"]

    name = models.CharField(max_length=30, validators=[v.MinLengthValidator(2)])
    surname = models.CharField(max_length=20, validators=[v.MinLengthValidator(2)])
    age = models.IntegerField(validators=[v.MinValueValidator(18)])

    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name="profile")


class ProfileStaffModel(BaseModel):
    class Meta:
        db_table = "staff_profile"
        ordering = ["id"]

    staff_type = models.CharField(max_length=11, choices=StaffTypeChoices.choices, blank=False, null=False)
    name = models.CharField(max_length=30, validators=[v.MinLengthValidator(2)])
    surname = models.CharField(max_length=20, validators=[v.MinLengthValidator(2)])
    age = models.IntegerField(validators=[v.MinValueValidator(18)])
    city = models.CharField(max_length=30, validators=[v.MinLengthValidator(2)])
    experience = models.IntegerField(validators=[v.MinValueValidator(0), v.MaxValueValidator(50)])
    phone = models.IntegerField()  # TODO
    public_email = models.EmailField()  # TODO

    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name="staff_profile")


