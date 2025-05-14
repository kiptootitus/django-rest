from django.contrib import admin
from .models import Book, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'Available', 'price' )
  search_fields = ('title', 'author', 'price')
  
  
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
  list_display = ('first_name','last_name','author_id')
  search_fields = ('first_name','last_name','author_id')