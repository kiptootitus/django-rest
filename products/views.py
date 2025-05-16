from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from .models import Product
from .serializers import ProductSerializer
from permissions import isStaffEditorPermission  # Ensure this exists and is implemented

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, isStaffEditorPermission]

# create view 
class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, isStaffEditorPermission]

    def perform_create(self, serializer):
        serializer.save()


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, isStaffEditorPermission]

    def perform_create(self, serializer):
        description = serializer.validated_data.get('description') or serializer.validated_data.get('name')
        serializer.save(description=description)
    
    
    
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



class ProductUpdateAPIView(generics.RetrieveUpdateAPIView):
    """
    This view allows you to retrieve a product by its ID (GET) and update it (PUT/PATCH).
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, isStaffEditorPermission]

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
