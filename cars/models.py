from django.db import models
from django.core import validators as v
from datetime import datetime

from core.models import BaseModel
from dealerships.models import CarDealershipModel


class CarModel(BaseModel):
    class Meta:
        db_table = "cars"
        ordering = ["id",]

    brand = models.CharField(max_length=20, validators=[v.MinLengthValidator(2)])
    model = models.CharField(max_length=20, validators=[v.MinLengthValidator(2)])
    year = models.IntegerField(validators=[v.MinValueValidator(1990), v.MaxValueValidator(datetime.now().year)])
    price = models.IntegerField(validators=[v.MinValueValidator(0), v.MaxValueValidator(1000000)])
    # photo = models.ImageField(upload_to=FileService.upload_car_photo, blank=True)

    car_dealership = models.ForeignKey(CarDealershipModel, on_delete=models.CASCADE, related_name="cars")

    # objects = CarManager()
