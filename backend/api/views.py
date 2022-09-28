from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductSerializer


@api_view(['GET'])
def home(request):
    """
    DRF API View
    """
    product = Product.objects.all().order_by('?').first()
    output_product = dict()

    # model instance -> python dict
    if product:
        # output_product = model_to_dict(
        #     product, fields=['title', 'price', 'sale_price'])
        output_product = ProductSerializer(product).data

    return Response(output_product)
