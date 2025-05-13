from django.urls import path

from . import views

urlpatterns = [
  path('', views.api_home, name='api'),
  path('listing/', views.ProductsListAPIView.as_view(), name="products-listing")
]