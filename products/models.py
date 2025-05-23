import random

from django.db.models import Q
from django.db import models
from config import PRODUCT_TYPE
from django.conf import settings

User = settings.AUTH_USER_MODEL
TAGS_MODEL_VALUES = ['cars', 'electronics', 'clothes', 'food']
class ProductQuerySet(models.QuerySet):
  def is_public(self):
    return self.filter(public=True)
  def search(self, query, user=None):
    lookup= Q(name__icontains=query) | Q(description__icontains=query)
    qs = self.is_public().filter(lookup)
    if user is not None:
      qs2 = self.filter(user=user).filter(lookup)

      qs = (qs2 | qs ).distinct()
    return qs


class ProductManager(models.Manager):
  def get_queryset(self, *args, **kwargs):
    return ProductQuerySet(self.model, using=self._db)

  def search(self, query, user=None):
    return self.get_queryset().search(query, user=user)



class Product(models.Model):
  user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
  name = models.CharField(max_length=250)
  description = models.TextField(blank= True, null=True)
  price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
  weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Missing?
  public = models.BooleanField(default=True)

  objects = ProductManager()
  def is_public(self) -> bool:
    return self.public
  def get_tags_lists(self):
    return [random.choice(TAGS_MODEL_VALUES)]
  def __str__(self):
    return self.name
  
  @property
  def sale_price(self):
    return f"{float(self.price)* 0.8:.2f}"
  
  def get_discount(self):
    return "123"