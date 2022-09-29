from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductSerializer


@api_view(['POST'])
def home(request):
    serialize_post = ProductSerializer(data=request.data)

    # validate post request data
    # raise exception, raised the exception if fields are missing
    if serialize_post.is_valid(raise_exception=True):
        created_post = serialize_post.save()
        post = serialize_post.data

        print(created_post)

        return Response(post)
