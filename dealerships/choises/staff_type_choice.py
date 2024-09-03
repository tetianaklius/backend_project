from django.db import models


class StaffTypeChoices(models.TextChoices):
    CarSeller = "CarSeller"
    CarMechanic = "CarMechanic",
    CarAdmin = "CarAdmin",
    CarManager = "CarManager"
