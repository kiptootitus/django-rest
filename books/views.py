from rest_framework import generics

from permissions import isStaffEditorPermission
from .models import Author, Book, BookAuthor
from .serializers import AuthorSerializer, BookSerializer, BookAuthorSerializer
from rest_framework import permissions, authentication
from rest_framework.authentication import SessionAuthentication
from drf.authentication import TokenAuthentication

class AuthorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'pk'
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [isStaffEditorPermission]

class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'
    permission_classes = [isStaffEditorPermission]


class BookAuthorListCreateAPIView(generics.ListCreateAPIView):
    queryset = BookAuthor.objects.all()
    serializer_class = BookAuthorSerializer

class BookAuthorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookAuthor.objects.all()
    serializer_class = BookAuthorSerializer
    lookup_field = 'pk'


class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, isStaffEditorPermission]
