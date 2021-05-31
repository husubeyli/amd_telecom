from rest_framework import serializers

from ..models import Product, Product_images, Marka




class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_images
        fields = '__all__'


class ProductMarkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marka
        fields = '__all__'


class SearchSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True, read_only=True)
    products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    images = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    products_images = serializers.SerializerMethodField()
    product_marka = serializers.SerializerMethodField()
    marka = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def get_products_images(self, instance):
        products_images = instance.images.all().order_by('-is_main')
        return ProductImageSerializer(products_images, many=True).data

    def get_product_marka(self, instance):
        product_marka = instance.marka
        return ProductMarkaSerializer(product_marka, many=True).data


class ProductSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    products_images = serializers.SerializerMethodField()
    product_marka = serializers.SerializerMethodField()
    priced = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_products_images(self, instance):
        products_images = instance.images.all().order_by('-is_main')
        return ProductImageSerializer(products_images, many=True).data

    def get_product_marka(self, instance):
        product_marka = instance.marka
        return ProductMarkaSerializer(product_marka, many=True).data

    def get_priced(self, instance):
        price = instance.get_price
        return price