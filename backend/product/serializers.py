from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    # if model method name is get_discount
    discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ['title', 'content', 'price', 'sale_price', 'discount']

    def get_discount(self, product):
        return product.get_discount()
