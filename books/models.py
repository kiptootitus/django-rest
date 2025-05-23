from django.db import models
from django.core.exceptions import ValidationError

from django.conf import settings


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    author_id = models.CharField(max_length=255, unique=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name


class Book(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, null=True, on_delete=models.SET_NULL)
    author = models.ManyToManyField(Author, through="BookAuthor")
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=99.99)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class BookAuthor(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'book'],
                name='unique_author_book'
            )
        ]

    def clean(self):
        if BookAuthor.objects.filter(author=self.author).exclude(pk=self.pk).count() >= 2:
            raise ValidationError("An author can't be linked to more than 2 books.")
        if BookAuthor.objects.filter(book=self.book).exclude(pk=self.pk).count() >= 2:
            raise ValidationError("A book can't have more than 2 authors.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
