from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('drf.urls')),
    path('api/search/', include('search.urls')),

    path('api/products/', include('products.urls')),
    path('api/books/', include('books.urls')),
    path('api/v2/', include('core.routers'))
    
]
