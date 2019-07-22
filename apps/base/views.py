from django.shortcuts import render
from rest_framework import viewsets
from .models import BlogCategory, Tags, BaseBlog
from .serializers import CategorySerializer, CategorySerializer3, TagsSerializer, BaseBlogSerialzier

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = BlogCategory.objects.all()
    serializer_class = CategorySerializer


class CategorysViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer3

    def get_queryset(self):
        return Category.objects.filter(category_level=1)


class TagsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TagsSerializer
    queryset = Tags.objects.all()


class BaseBlogViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BaseBlogSerialzier
    queryset = BaseBlog.objects.all()
