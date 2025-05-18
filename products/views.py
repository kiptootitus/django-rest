from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import generics, status, permissions, mixins
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication

from drf.authentication import TokenAuthentication
from drf.mixins import StaffEditorPermissionMixin, UserQuerySetMixin
from .models import Product
from .serializers import ProductSerializer

class ProductDetailAPIView(UserQuerySetMixin, StaffEditorPermissionMixin, generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

# create view 
class ProductCreateAPIView(StaffEditorPermissionMixin, mixins.ListModelMixin, generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save()


class ProductCreateListAPIView(UserQuerySetMixin, StaffEditorPermissionMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    lookup_field = 'pk'


    def perform_create(self, serializer):
        description = serializer.validated_data.get('description') or serializer.validated_data.get('name')
        serializer.save(user = self.request.user, description=description)

    # def get_queryset(self, *args, **kwargs):
    #     qs= super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     user = request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     return qs.filter(user=self.request.user)
    
    
    
@api_view(["GET", "POST"])
def product_alt_view(request, pk=None):
    if request.method == "GET":
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj).data
            return Response(data)

        qs = Product.objects.all()
        data = ProductSerializer(qs, many=True).data
        return Response(data)

    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)



class ProductUpdateAPIView(UserQuerySetMixin, StaffEditorPermissionMixin, generics.RetrieveUpdateAPIView):
    """
    This view allows you to retrieve a product by its ID (GET) and update it (PUT/PATCH).
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get_object(self):
        """
        Optionally override get_object to use a custom lookup,
        or simply rely on the default which uses the 'pk' lookup field.
        """
        pk = self.kwargs.get('pk')
        return get_object_or_404(Product, pk=pk)

    def update(self, request, *args, **kwargs):
        """
        Optionally override update to customize update behavior.
        This method demonstrates explicitly saving the instance
        and returning the updated data.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_200_OK)
