from rest_framework.routers import DefaultRouter

from books.viewsets import BookCreateViewSet, BookGenericViewSet


router = DefaultRouter()

router.register('books', BookCreateViewSet, basename='books')
router.register('book-update', BookGenericViewSet, basename='book-update')
print(router.urls)
urlpatterns = router.urls