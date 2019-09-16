import django_filters
from .models import BaseCategory, BaseBlog


class CategoryFilter(django_filters.rest_framework.FilterSet):
    min_datetime = django_filters.DateTimeFilter(name='create_time', lookup_expr='gte')
    max_datetime = django_filters.DateTimeFilter(name='create_time', lookup_expr='lte')
    class Meta:
        model = BaseCategory
        fields = ('index', 'min_datetime', 'max_datetime')

class BlogFilter(django_filters.rest_framework.FilterSet):
    min_datetime = django_filters.DateTimeFilter(name='create_time', lookup_expr='gte')
    max_datetime = django_filters.DateTimeFilter(name='create_time', lookup_expr='lte')
    class Meta:
        model = BaseBlog
        fields = ('min_datetime', 'max_datetime')
