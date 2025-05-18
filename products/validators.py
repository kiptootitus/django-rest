from rest_framework import serializers

from .models import Product


def validate_name(self, value):
    request = self.context.get('request')
    user = request.user

    # Exclude the current instance when updating
    qs = Product.objects.filter(user=user, name__iexact=value)
    if self.instance:
        qs = qs.exclude(pk=self.instance.pk)

    if qs.exists():
        raise serializers.ValidationError(f"This name '{value}' already exists, choose another one.")
    return value
