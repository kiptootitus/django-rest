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
            'pk',
            'name',
            'description',
            'price',
            'weight',
            'sale_price',
            'my_discount',
        ]
        read_only_fields = ['edit_url', 'my_discount']

    def validate_name(self, value):
        request = self.context.get('request')
        user = request.user if request else None
        qs = Product.objects.filter(name__iexact=value)
        if user and user.is_authenticated:
            qs = qs.filter(user=user)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError(f"{value} already exists. This field must be unique.")
        return value

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
