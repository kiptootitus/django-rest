from django.urls import path

from . import views

urlpatterns = [
  path('detail/<int:pk>', views.ProductDetailAPIView.as_view(), name='product-detail'),
  path('create/', views.ProductCreateAPIView.as_view(), name='product-create'),
  path('list/', views.ProductListAPIView.as_view(), name='product-list'),
  path('update/<int:pk>', views.product_alt_view, name='product-update')


]