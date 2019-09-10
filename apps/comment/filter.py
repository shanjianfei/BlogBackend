import django_filters
from .models import Comment

class CommentFilter(django_filters.rest_framework.FilterSet):
    article_id = django_filters.NumberFilter(name='article')

    class Meta:
        model = Comment
        fields = ('article_id', 'super_comment', 'belong_root', 'is_root')