import django_filters
from .models import BaseCategory


class CategoryFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = BaseCategory
        fields = ('index',)
