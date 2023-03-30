# from django.http import JsonResponse
# not using from django.http because that needs a csrf token that we don't need8
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict # cuts down the tedious work

from products.models import Product
from products.serializers import ProductSerializer

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid():
        instance  = serializer.save()
        print(instance)
    # here serializer helps in validating the data  
    return Response(serializer.data)