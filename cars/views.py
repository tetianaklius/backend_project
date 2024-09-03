from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from cars.models import CarModel
from cars.serializers import CarSerializer


class CarListView(ListAPIView):
    """
        Get all cars
    """
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    permission_classes = [AllowAny]


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
      get:
          get car details
      put:
          update car
      patch:
          partial update car
      delete:
          delete car
    """
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

    def get_permissions(self):
        if self.request.method in ["POST", "PUT", "PATCH"]:
            return [IsAuthenticated()]  #TODO
        if self.request.method == "DELETE":
            return [IsAuthenticated()]  # TODO
