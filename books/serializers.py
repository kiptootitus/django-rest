from .models import Author, Book, BookAuthor
from rest_framework import serializers
from rest_framework.reverse import reverse
from drf.serializers import UserPublicSerializer

class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Author
    fields = [
      'first_name',
      'last_name',
      'author_id',
    ]


class BookSerializer(serializers.ModelSerializer):
  user = UserPublicSerializer(read_only=True)
  edit_url = serializers.SerializerMethodField(read_only=True)
  authors = serializers.PrimaryKeyRelatedField(
    queryset=Author.objects.all(),
    many=True,
    write_only=True
  )
  author_names = serializers.SerializerMethodField(read_only=True)
  class Meta:
    model = Book
    fields = [
      'edit_url',
      'user',
       'authors',
      'author_names',
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

  def validate_title(self, value):
    request = self.context.get('request')
    user = request.user
    if Book.objects.filter(user=user, title__iexact=value).exists():
      raise serializers.ValidationError("You already have a book with this title.")
    return value

  def get_author_names(self, obj):
      return [author.full_name for author in obj.author.all()]

  def create(self, validated_data):
    authors = validated_data.pop('authors', [])
    book = Book.objects.create(**validated_data)
    for author in authors:
      BookAuthor.objects.create(book=book, author=author)
    return book

class BookAuthorSerializer(serializers.ModelSerializer):
  book_title = serializers.CharField(source='book.title', read_only=True)
  author_name = serializers.SerializerMethodField()

  class Meta:
    model = BookAuthor
    fields = ['id', 'book', 'book_title', 'author', 'author_name']

  def get_author_name(self, obj):
    return f"{obj.author.first_name} {obj.author.last_name}"
