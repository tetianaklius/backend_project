from django.db import models
from django.core import validators as v
from datetime import datetime

from core.models import BaseModel
from users.models import ProfileModel, UserModel, ProfileStaffModel


class CarDealershipModel(BaseModel):
    class Meta:
        db_table = "car_dealerships"
        ordering = ["id"]

    name = models.CharField(max_length=20)
    city = models.CharField(max_length=30, validators=[v.MinLengthValidator(2)])


class CarSellerModel(ProfileModel):
    class Meta:
        db_table = "cd_sellers"
        ordering = ["id"]
    staff_profile = models.OneToOneField(ProfileStaffModel, on_delete=models.CASCADE, related_name="cd_seller_profile")
    # photo = models.ImageField(upload_to=FileService.upload_car_photo, blank=True) #TODO
    car_dealership = models.ForeignKey(CarDealershipModel, on_delete=models.CASCADE, related_name="sellers")


class CarMechanicModel(ProfileModel):
    class Meta:
        db_table = "cd_mechanics"
        ordering = ["id"]
    staff_profile = models.OneToOneField(ProfileStaffModel, on_delete=models.CASCADE, related_name="cd_mechanic_profile")
    car_dealership = models.ForeignKey(CarDealershipModel, on_delete=models.CASCADE, related_name="mechanics")


class CarAdminModel(ProfileModel):
    class Meta:
        db_table = "cd_admins"
        ordering = ["id"]
    staff_profile = models.OneToOneField(ProfileStaffModel, on_delete=models.CASCADE, related_name="cd_admin_profile")
    car_dealership = models.ForeignKey(CarDealershipModel, on_delete=models.CASCADE, related_name="admins")


class CarManagerModel(ProfileModel):
    class Meta:
        db_table = "cd_managers"
        ordering = ["id"]
    staff_profile = models.OneToOneField(ProfileStaffModel, on_delete=models.CASCADE, related_name="cd_manager_profile")
    car_dealership = models.ForeignKey(CarDealershipModel, on_delete=models.CASCADE, related_name="managers")


