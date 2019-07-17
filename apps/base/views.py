from django.shortcuts import render
from rest_framework import viewsets
from .models import BlogCategory
from .serializers import CategorySerializer, CategorySerializer3

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = BlogCategory.objects.all()
    serializer_class = CategorySerializer


class CategorysViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer3

    def get_queryset(self):
        return Category.objects.filter(category_level=1)
