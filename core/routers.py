from rest_framework.routers import DefaultRouter

from books.viewsets import BookCreateViewSet, BookGenericViewSet
from products.viewsets import ProductCreateViewSet, ProductGenericViewSet

router = DefaultRouter()

router.register('books', BookCreateViewSet, basename='booklists')
router.register('update', BookGenericViewSet, basename='book-update')
router.register('products', ProductGenericViewSet, basename='product-lists')
router.register('create', ProductCreateViewSet, basename='product-create')

urlpatterns = router.urls