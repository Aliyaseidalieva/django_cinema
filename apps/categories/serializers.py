from rest_framework import serializers

from .models import Category

class CategorySerializer(serializers.ModelSerializer):

    name = serializers.CharField(required=True)
    url = serializers.SlugField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'url']
