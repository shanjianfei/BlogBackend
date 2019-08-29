from django.shortcuts import render
from rest_framework import viewsets, mixins, filters
from rest_framework import pagination
from rest_framework.response import Response
from django_filters import rest_framework
from .models import BaseCategory, BlogCategory, Tags, BaseBlog
from .serializers import BaseCategorySerializer, CategoryLevelSerializer, TagsSerializer, BaseBlogSerialzier

# Create your views here.

class CategorySingleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogCategory.objects.filter(category_level=1)
    serializer_class = CategoryLevelSerializer


# 获取总分类
class CategoryLevelViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = BaseCategorySerializer
    queryset = BaseCategory.objects.all()


class TagsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TagsSerializer
    queryset = Tags.objects.all()


class BaseBlogViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BaseBlogSerialzier
    queryset = BaseBlog.objects.all()
    filter_backends = (rest_framework.DjangoFilterBackend, filters.OrderingFilter)
    ordering_field = ('create_time', 'click')
