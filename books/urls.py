from django.urls import path
from .views import (
    AuthorListCreateAPIView, AuthorRetrieveUpdateDestroyAPIView,
    BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView,
    BookAuthorListCreateAPIView
)

urlpatterns = [
    path('authors/', AuthorListCreateAPIView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroyAPIView.as_view(), name='author-detail'),
    path('book/', BookListCreateAPIView.as_view(), name='books-detail'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-update'),
    path('book-authors/', BookAuthorListCreateAPIView.as_view(), name='bookauthor-list-create'),
]
