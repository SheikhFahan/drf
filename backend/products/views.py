from rest_framework import generics , mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http_404
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer
from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin


class ProductListCreateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer    

    def perform_create(self, serializer):
        # serializer.save(user = self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None 
        if content is None:
            content = title 
        serializer.save(user = self.request.user, content = content)

    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset()
    #     user = self.request.user 

    #     if not user.is_authenticated:
    #         return Product.objects.none()

    #     return qs.filter(user = user)

product_list_create_view = ProductListCreateAPIView.as_view()


class ProductDetailAPIView(
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # there is a obj variable with it through-out

product_detail_view = ProductDetailAPIView.as_view()

class ProductUpdateAPIView(
    StaffEditorPermissionMixin,
    generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    look_up = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

product_update_view = ProductUpdateAPIView.as_view()

class ProductDeleteAPIView(
    StaffEditorPermissionMixin,
    generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    look_up = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
product_delete_view = ProductDeleteAPIView.as_view()


class ProductMixinAPIVeiw(mixins.ListModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView, 
    mixins.CreateModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    # this needs to be hre cause this is how the fn in designed

    def get(self,request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, args, kwargs)
        return self.list(request,  *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)


product_mixin_view = ProductMixinAPIVeiw.as_view()



# @api_view(['GET', 'POST'])
# def product_alt_view(request, pk = None, *args, **kwargs):
#     """ this view does the work of create list detail """
#     if request.method == 'GET':
#         if pk is not None:
#             obj = get_object_or_404(Product, pk = pk) #checks for object in the db
#             data = ProductSerializer(obj, many= False).data
#             return Response(data)

#         queryset = Product.objects.all()
#         data = ProductSerializer(queryset, many = True).data
#         return Response(data)

#     if request.method == 'POST':
#         serializer = ProductSerializer(data = request.data)
#         if serializer.is_valid(raise_exception = True):
#             title = serializer.validated_data.get('title')
#             content = serializer.validated_data.get('content') or None 
#             if content is None:
#                 content = title 
#             serializer.save(content = content)
#             return Response(serializer.data)
#         # here serializer helps in validating the data  
#         return Response(serializer.data)

