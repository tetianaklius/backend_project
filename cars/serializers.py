from rest_framework import serializers

from cars.models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ("brand", "model", "year", "price", "created_at", "updated_at")
