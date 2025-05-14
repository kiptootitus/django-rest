from .models import Author, Book, BookAuthor
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = [
      'author',
      'title',
      'price',
      'description',
      'available'      
    ]
    

class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Author
    fields = [
      'first_name',
      'last_name',
      'author_id',
    ]
    
    
class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAuthor
        fields = '__all__'