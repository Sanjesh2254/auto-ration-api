from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, manfacturer, hardware
from .serializers import ProductSerializer,ManfacturerSerializer, hardwareSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class manfacturerViewSet(viewsets.ModelViewSet):
    queryset = manfacturer.objects.all()
    serializer_class = ManfacturerSerializer

class hardwareViewSet(viewsets.ModelViewSet):
    queryset = hardware.objects.all()
    serializer_class = hardwareSerializer
    @action(detail=False, methods=['get'], url_path='latestdata')
    def latest(self, request):
        latest_hardware = self.queryset.order_by('-id').first()
        if latest_hardware:
            serializer = self.get_serializer(latest_hardware)
            return Response(serializer.data)
        return Response({"detail": "No hardware data available."})



    