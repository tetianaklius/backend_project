from rest_framework import serializers

from dealerships.models import CarDealershipModel
from cars.serializers import CarSerializer


class CarDealershipSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = CarDealershipModel
        fields = ("id", "name", "created_at", "updated_at", "cars")
        # depth = 1  #TODO
