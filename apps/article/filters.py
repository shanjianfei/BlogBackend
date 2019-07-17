from article.models import Article
import django_filters


class ArticleListFilter(django_filters.rest_framework.FilterSet):
    # contains 包含， 但是不忽略大小写， icontains 忽略大小写
    title = django_filters.CharFilter(name='title', lookup_expr='icontains')
    category = django_filters.CharFilter(name='category__category', lookup_expr='icontains')
    min_datetime = django_filters.DateTimeFilter(name='create_time', lookup_expr='gte')
    max_datetime = django_filters.DateTimeFilter(name='create_time', lookup_expr='lte')
    tags = django_filters.CharFilter(name='tags__label', lookup_expr='icontains')
    istop = django_filters.BooleanFilter(name='istop', lookup_expr='exact')
    isrecommend = django_filters.BooleanFilter(name='isrecommend', lookup_expr='exact')

    class Meta:
        model = Article
        fields = ('title', 'category', 'min_datetime', 'max_datetime', 'tags', 'istop', 'isrecommend')


# class CommentFilter(django_filters.rest_framework.FilterSet):
#     article_id = django_filters.NumberFilter(name='article')

#     class Meta:
#         model = Comment
#         fields = ('article_id', )


# class TagFilter(django_filters.rest_framework.FilterSet):
#     def tags(self, queryset, name, value):
#         queryset.all()
