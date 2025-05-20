from rest_framework import generics
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer
from .client import perform_search

class SearchListView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')        
        results = perform_search(query)
        return Response(results)

class SearchOldListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        results = Product.objects.none()
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(q, user=user)
        return results
