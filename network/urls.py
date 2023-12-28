from django.urls import path
from rest_framework.routers import DefaultRouter
from network.apps import NetworkConfig

from network.views import (ManufacturerAPIView, ManufacturerCreateAPIView,
                           ManufacturerRetrieveAPIView, ManufacturerUpdateAPIView, ManufacturerDestroyAPIView,
                           SupplierViewSet)

app_name = NetworkConfig.name

router = DefaultRouter()
router.register(r'supplier', SupplierViewSet, basename='supplier')
urlpatterns = [

    path('manufacturer/', ManufacturerAPIView.as_view(), name='manufacturer_list'),
    path('manufacturer/create', ManufacturerCreateAPIView.as_view(), name='manufacturer_create'),
    path('manufacturer/<int:pk>', ManufacturerRetrieveAPIView.as_view(), name='manufacturer_get'),
    path('manufacturer/update/<int:pk>', ManufacturerUpdateAPIView.as_view(), name='manufacturer_update'),
    path('manufacturer/delete/<int:pk>', ManufacturerDestroyAPIView.as_view(), name='manufacturer_delete'),



] + router.urls