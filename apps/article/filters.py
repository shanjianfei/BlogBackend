from .models import ArticleModel, Comment
import django_filters


class ArticleListFilter(django_filters.rest_framework.FilterSet):
    # contains 包含， 但是不忽略大小写， icontains 忽略大小写
    title = django_filters.CharFilter(name='title', lookup_expr='icontains')
    category = django_filters.CharFilter(name='category__catgory', lookup_expr='icontains')
    min_datetime = django_filters.DateTimeFilter(name='create_time', lookup_expr='gte')
    max_datetime = django_filters.DateTimeFilter(name='create_time', lookup_expr='lte')

    class Meta:
        model = ArticleModel
        fields = ('title', 'category', 'min_datetime', 'max_datetime')


class CommentFilter(django_filters.rest_framework.FilterSet):
    article_id = django_filters.NumberFilter(name='article')

    class Meta:
        model = Comment
        fields = ('article_id', )
