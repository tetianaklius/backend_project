from django.urls import path

from users.views import UserListCreateView, UserBlockView, UserUnBlockView, UserToMainManagerView, UserToStaffView

urlpatterns = [
    path("", UserListCreateView.as_view()),
    path("/<int:pk>/main_manager", UserToMainManagerView.as_view()),
    path("/<int:pk>/dealer_center_staff", UserToStaffView.as_view()),
    path('/<int:pk>/block', UserBlockView.as_view()),
    path('/<int:pk>/unblock', UserUnBlockView.as_view()),
]
