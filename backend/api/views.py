import json
from django.forms.models import model_to_dict
from django.http import JsonResponse

from product.models import Product


def home(request):
    product = Product.objects.all().order_by('?').first()
    output_product = dict()

    # model instance -> python dict
    if product:
        output_product = model_to_dict(product)

    return JsonResponse(output_product)
