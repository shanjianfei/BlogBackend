from article.models import Article
from comment.models import Comment
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    comment_count = serializers.SerializerMethodField()

    def get_comment_count(self, instance):
        return Comment.objects.filter(article=instance).count()
        # return instance.comment_set.all().count()

    class Meta:
        model = Article
        fields = ('id', 'title', 'desc', 'create_time',
                  'update_time', 'tags', 'author', 'click', 'like', 'category', 'istop', 'cover', 'isrecommend', 'comment_count')
        read_only_fields = ('id', 'title', 'desc', 'create_time',
                            'update_time', 'tags', 'author', 'cover',
                            'click', 'like', 'category', 'istop', 'picture', 'isrecommend', 'comment_count')


class ArticleLikeSerializer(serializers.Serializer):
    like = serializers.BooleanField(required=True)
