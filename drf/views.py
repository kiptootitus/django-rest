from django.forms import model_to_dict
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
import json
from drf.mixins import StaffEditorPermissionMixin
from rest_framework.authentication import SessionAuthentication

from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer
from rest_framework import generics
from rest_framework import permissions

from drf.authentication import TokenAuthentication

@api_view(['GET','POST'])
def api_home(request, *args, **kwargs):
  serializer = ProductSerializer(data =request.data)
  if serializer.is_valid():
    instance = serializer.save()
    
  
  return Response(serializer.data)



class ProductsListAPIView(StaffEditorPermissionMixin, generics.ListAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  authentication_classes = [SessionAuthentication, TokenAuthentication]
  permission_classes = [permissions.IsAdminUser]