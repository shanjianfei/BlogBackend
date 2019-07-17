from rest_framework import serializers
from .models import BlogCategory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = '__all__'

class CategorySerializer2(serializers.ModelSerializer):
    sub_category = CategorySerializer(many=True)
    class Meta:
        model = BlogCategory
        fields = '__all__'

class CategorySerializer3(serializers.ModelSerializer):
    sub_category = CategorySerializer2(many=True)
    class Meta:
        model = BlogCategory
        fields = '__all__'
