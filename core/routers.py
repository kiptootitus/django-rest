from rest_framework.routers import DefaultRouter

from books.viewsets import BookCreateViewSet, BookGenericViewSet


router = DefaultRouter()

router.register('books', BookCreateViewSet, basename='booklists')
router.register('book-update', BookGenericViewSet, basename='book-update')
urlpatterns = router.urls