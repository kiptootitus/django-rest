from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register
from .models import Product

@register(Product)
class ProductIndex(AlgoliaIndex):
    should_index = 'is_public'
    def get_attributes(self, instance):
        return {
            'user': instance.user.username if instance.user else None,
            'name': instance.name,
            'description': instance.description,
            'price': float(instance.price),
            'weight': float(instance.weight) if instance.weight else None,
            'public': instance.public,
        }
