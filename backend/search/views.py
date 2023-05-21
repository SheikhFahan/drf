from rest_framework import generics
from rest_framework.response import Response

from products.models import Product 
from products.serializers import ProductSerializer

from . import client

class SearchListView(generics.GenericAPIView):
    
    def get(self, request,*args, **kwargs):
        user = None
        if request.user.is_authenticated:
            user = request.user.username
        query = request.GET.get('q')
        print(str(request.GET.get('public')))
        public = str(request.GET.get('public')) != "0"
        # public = True
        # if request.GET.get('public') is not None:
        #     public = str(request.GET.get('public'))

        tag = request.GET.get('tag') or None
        if not query:
            return Response('', status=4004)
        results = client.perform_search(query, tags = tag, user = user , public = public)
        return Response(results)

class SearchListOldView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        user = None
        results = Product.objects.none()
        if q is not None:
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(q, user=user)
        return results