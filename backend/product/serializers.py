from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'content', 'price', 'sale_price', 'discount']


# you can create as many serializers as you want for one model/table
