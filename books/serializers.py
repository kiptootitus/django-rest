from .models import Author, Book, BookAuthor
from rest_framework import serializers
from rest_framework.reverse import reverse

class BookSerializer(serializers.ModelSerializer):
  edit_url = serializers.SerializerMethodField(read_only=True)
  # url = serializers.HyperlinkedIdentityField(view_name='books-detail')
  class Meta:
    model = Book
    fields = [
      'edit_url',
      # 'url',
      # 'author',
      'title',
      'price',
      'description',
      'available'      
    ]
  def get_edit_url(self, obj):
    request = self.context.get('request')
    if request is None:
      return None
    return reverse("book-update", kwargs={"pk": obj.pk}, request=request)
    
    

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