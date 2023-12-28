import django_filters
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, viewsets
from network.models import Manufacturer, Supplier
from network.serializers import ManufacturerSerializer, SupplierSerializer


class ManufacturerAPIView(generics.ListAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ManufacturerCreateAPIView(generics.CreateAPIView):
    serializer_class = ManufacturerSerializer


class ManufacturerRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()


class ManufacturerUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()


class ManufacturerDestroyAPIView(generics.DestroyAPIView):
    queryset = Manufacturer.objects.all()


class SupplierFilter(django_filters.FilterSet):
    """ Фильтр объектов по определенной стране"""
    class Meta:
        model = Supplier
        fields = ['country']


class SupplierViewSet(viewsets.ModelViewSet):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = SupplierFilter


