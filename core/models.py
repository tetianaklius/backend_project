from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

