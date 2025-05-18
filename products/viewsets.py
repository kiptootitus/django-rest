from rest_framework import mixins, viewsets

from drf.mixins import StaffEditorPermissionMixin
from .models import Product
from .serializers import ProductSerializer
from rest_framework.authentication import SessionAuthentication
from drf.authentication import TokenAuthentication

class ProductGenericViewSet(StaffEditorPermissionMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'
  authentication_classes = [SessionAuthentication, TokenAuthentication]

class ProductCreateViewSet(viewsets.ModelViewSet):
  '''
 This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    '''
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'
  
  