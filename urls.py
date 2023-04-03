from django.urls import path
from .views import (
    TankenListAPIView,
    TankenRetrieveAPIView,
    TankenCreateAPIView,
    TankenRetrieveUpdateAPIView,
    TankenDestroyAPIView,
    TankenListView,
    TankenCreateView
)

urlpatterns = [
    path("", TankenListAPIView.as_view(), name="tanken_list"),
    path("list/", TankenListView.as_view(), name="tanklist"),
    path("new/", TankenCreateView.as_view(), name="tanken_new"),
    path("<int:id>/", TankenRetrieveAPIView.as_view(), name="tanken_detail"),
    path("create/", TankenCreateAPIView.as_view(), name="tanken_create"),
    path("update/<int:id>/", TankenRetrieveUpdateAPIView.as_view(), name="tanken_update"),
    path("delete/<int:id>/", TankenDestroyAPIView.as_view(), name="tanken_delete"),
]
