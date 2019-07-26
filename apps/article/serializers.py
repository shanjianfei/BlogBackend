from article.models import Article
from comment.models import Comment
from comment.serializers import CommentSerializer
from base.serializers import TagsSerializer
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(many=True)
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    comment_count = serializers.SerializerMethodField()

    def get_comment_count(self, instance):
        return Comment.objects.filter(article=instance).count()
        # return instance.comment_set.all().count()

    class Meta:
        model = Article
        fields = '__all__'


class ArticleDetailSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Article
        fields = ('title', 'desc', 'content', 'create_time',
                  'update_time', 'tags', 'author', 'click', 'like', 'comments', 'comment_enable')


class ArticleLikeSerializer(serializers.Serializer):
    like = serializers.BooleanField(required=True)
