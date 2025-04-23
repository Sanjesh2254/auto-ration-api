from rest_framework import serializers
from .models import Product, manfacturer, hardware

class ManfacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = manfacturer
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class hardwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = hardware
        fields = '__all__'
