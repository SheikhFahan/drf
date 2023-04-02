from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http_404
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer    

    def perform_create(self, serializer):
        # serializer.save(user = self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None 
        if content is None:
            content = title 
        serializer.save(content = content)

product_list_create_view = ProductListCreateAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # there is a obj variable with it through-out

product_detail_view = ProductDetailAPIView.as_view()


@api_view(['GET', 'POST'])
def product_alt_view(request, pk = None, *args, **kwargs):
    if request.method == 'GET':
        if pk is not None:
            obj = get_object_or_404(Product, pk = pk) #checks for object in the db
            data = ProductSerializer(obj, many= False).data
            return Response(data)

        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many = True).data
        return Response(data)

    if request.method == 'POST':
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None 
            if content is None:
                content = title 
            serializer.save(content = content)
            return Response(serializer.data)
        # here serializer helps in validating the data  
        return Response(serializer.data)

