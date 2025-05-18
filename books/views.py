from rest_framework import generics
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication
from drf.authentication import TokenAuthentication

from drf.mixins import StaffEditorPermissionMixin, UserQuerySetMixin
from .models import Author, Book, BookAuthor
from .serializers import AuthorSerializer, BookSerializer, BookAuthorSerializer


class AuthorListCreateAPIView(StaffEditorPermissionMixin, generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]


class AuthorRetrieveUpdateDestroyAPIView(StaffEditorPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'pk'
    authentication_classes = [SessionAuthentication, TokenAuthentication]


class BookListCreateAPIView(UserQuerySetMixin,StaffEditorPermissionMixin, generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'
    authentication_classes = [SessionAuthentication, TokenAuthentication]


class BookRetrieveUpdateDestroyAPIView(StaffEditorPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'
    authentication_classes = [SessionAuthentication, TokenAuthentication]


class BookAuthorListCreateAPIView(StaffEditorPermissionMixin, generics.ListCreateAPIView):
    queryset = BookAuthor.objects.all()
    serializer_class = BookAuthorSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
