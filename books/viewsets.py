from rest_framework import viewsets
from rest_framework import mixins
from .models import Author, Book, BookAuthor
from .serializers import AuthorSerializer, BookSerializer, BookAuthorSerializer


class BookCreateViewSet(viewsets.ModelViewSet):
  '''
 This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    '''
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  lookup_field = 'pk'
  
  
  class BookGenericViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk' 