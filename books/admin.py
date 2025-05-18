from django.contrib import admin
from .models import Book, Author, BookAuthor

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_authors', 'available', 'price')
    search_fields = ['title']


    def get_authors(self, obj):
        return ", ".join([str(author) for author in obj.author.all()])
    get_authors.short_description = 'Authors'

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'author_id')
    search_fields = ['first_name', 'last_name', 'author_id']

@admin.register(BookAuthor)
class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ('author', 'book', 'date_joined')
