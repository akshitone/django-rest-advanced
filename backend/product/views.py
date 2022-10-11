from rest_framework import generics

from product.models import Product
from product.serializers import ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    print(queryset)
    serializer_class = ProductSerializer


product_detail_view = ProductDetailAPIView.as_view()
