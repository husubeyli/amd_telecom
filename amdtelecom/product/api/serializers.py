from rest_framework import serializers

from ..models import Product, Product_images


class ProductSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    images = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    marka = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    # def to_representation(self, instance):
    #     data = super(ProductSerializer, self).to_representation(instance)
    #     # manipulate data here 
    #     return data

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_images


        fields = '__all__'