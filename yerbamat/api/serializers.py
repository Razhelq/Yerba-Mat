from rest_framework import serializers
from yerba_mat.models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ("name", "description", "price", "amount", "rate", "category")
