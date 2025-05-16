from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
  path('auth/', obtain_auth_token, name='authentication'),
  path('', views.api_home, name='api'),
  path('listing/', views.ProductsListAPIView.as_view(), name="products-listing")
]