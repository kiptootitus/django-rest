from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField()
    edit_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'edit_url',
            'name',
            'description',
            'price',
            'weight',
            'sale_price',
            'my_discount',
        ]
        read_only_fields = ['edit_url', 'my_discount']

    def get_my_discount(self, obj):
        try:
            return obj.get_discount()
        except AttributeError:
            return None  # Or handle the error as needed

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('product-detail', kwargs={'pk': obj.pk}, request=request)

    def create(self, validated_data):
        # Handle weight if needed, e.g., validate or transform it
        weight = validated_data.get('weight')  # Use get to avoid KeyError
        # Create the object
        return super().create(validated_data)
      
    def update(self, instance, validated_data):
      instance.name = validated_data.get('name')
      instance.description = validated_data.get('description')
      instance.price = validated_data.get('price')
      instance.name = validated_data.get('weight')
      
      return instance
                        