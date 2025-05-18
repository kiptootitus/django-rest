from rest_framework import serializers
from rest_framework.reverse import reverse

from drf.serializers import UserPublicSerializer
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField()
    edit_url = serializers.SerializerMethodField()
    owner =  UserPublicSerializer(source='user',read_only=True)
    public = serializers.BooleanField()
    class Meta:
        model = Product
        fields = [
            'edit_url',
            'owner',
            'pk',
            'public',
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
            return None

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('product-detail', kwargs={'pk': obj.pk}, request=request)
