from django.db import models
from config import PRODUCT_TYPE
from core.settings import User

class Product(models.Model):
  user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
  name = models.CharField(max_length=250)
  description = models.TextField(blank= True, null=True)
  price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
  weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Missing?
  
  def __str__(self):
    return self.name
  
  @property
  def sale_price(self):
    return f"{float(self.price)* 0.8:.2f}"
  
  def get_discount(self):
    return "123"