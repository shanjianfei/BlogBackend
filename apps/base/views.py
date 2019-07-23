from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework import pagination
from rest_framework.response import Response
from .models import BlogCategory, Tags, BaseBlog
from .serializers import CategoryLevelSerializer, CategorySerializer, TagsSerializer, BaseBlogSerialzier

# Create your views here.

class CategroyPagination(pagination.PageNumberPagination):
    page_size = 1
    max_page_size = 1
    def get_paginated_response(self, data):
        if data:
            data = data[0]['category']
        else:
            data = []
        return Response({'result': data})


class CategoryLevelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogCategory.objects.all()
    serializer_class = CategoryLevelSerializer


# 获取一级分类
class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CategorySerializer
    queryset = BlogCategory.objects.all()
    pagination_class = CategroyPagination


class TagsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TagsSerializer
    queryset = Tags.objects.all()


class BaseBlogViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BaseBlogSerialzier
    queryset = BaseBlog.objects.all()
