from django.urls import path

from dealerships.views import CarDealershipListCreateView, CarDealershipAddCarView

urlpatterns = [
    path("", CarDealershipListCreateView.as_view()),
    path("/<int:pk>/cars", CarDealershipAddCarView.as_view()),
]
