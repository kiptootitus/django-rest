from django.forms import model_to_dict
from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer
@api_view(['GET','POST'])
def api_home(request, *args, **kwargs):
  instance = Product.objects.all().order_by("?").first()
  data = {}
  if instance:
  #  data = model_to_dict(model_data, fields=['id', 'name', 'price'])
    data = ProductSerializer(instance).data
  return Response(data)