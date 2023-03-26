# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict # cuts down the tedious work

from products.models import Product
from products.serializers import ProductSerializer

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(instance, fields = ['id', 'title', 'price'])
        # the line above does the work of the four lines below
        # data['id'] = model_data.i  d
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        data = ProductSerializer(instance).data
    return Response(data)