from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('drf.urls')),
    path('api/products/', include('products.urls')),
    path('api/books/', include('books.urls')),
    
]
