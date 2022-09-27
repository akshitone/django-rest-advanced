from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Product


@api_view(['GET'])
def home(request):
    """
    DRF API View
    """
    product = Product.objects.all().order_by('?').first()
    output_product = dict()

    # model instance -> python dict
    if product:
        output_product = model_to_dict(product, fields=['title', 'price'])

    return Response(output_product)
