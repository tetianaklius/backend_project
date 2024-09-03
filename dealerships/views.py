from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# from core.permissions.is_admin_or_write_only import IsAdminOrWriteOnly
from dealerships.models import CarDealershipModel
from dealerships.serializers import CarDealershipSerializer
from cars.serializers import CarSerializer
# from users.serializers import ProfileStaffSerializer


class CarDealershipListCreateView(ListCreateAPIView):
    serializer_class = CarDealershipSerializer
    queryset = CarDealershipModel.objects.all()
    permission_classes = (AllowAny,)
    # permission_classes = # (IsAdminOr/WriteOnly,) #TODO


class CarDealershipAddCarView(GenericAPIView):
    queryset = CarDealershipModel.objects.all()
    serializer_class = CarDealershipSerializer

    def post(self, *args, **kwargs):
        car_dealership = self.get_object()
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(car_dealership=car_dealership)
        cd_serializer = CarDealershipSerializer(car_dealership)
        return Response(cd_serializer.data, status.HTTP_201_CREATED)


# class CarDealershipAddSellerView(GenericAPIView):
#     queryset = CarDealershipModel.objects.all()
#     serializer_class = CarDealershipSerializer
#
#     def post(self, *args, **kwargs):
#         car_dealership = self.get_object()
#         data = self.request.data
#         serializer = ProfileStaffSerializer(data=data)   #
#         serializer.is_valid(raise_exception=True)
#         serializer.save(car_dealership=car_dealership)
#         cd_serializer = CarDealershipSerializer(car_dealership)
#         return Response(cd_serializer.data, status.HTTP_201_CREATED)
