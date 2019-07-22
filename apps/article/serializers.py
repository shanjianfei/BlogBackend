from article.models import Article
from rest_framework import serializers


class ArticleListSerializer(serializers.ModelSerializer):
    # comment = len(CommentSerializer(many=True).data)
    # tags = TagNormalSerializer(many=True)

    class Meta:
        model = Article
        # fields = ('title', 'content', 'create_time', 'update_time',
        # 'catgory', 'author', 'picture', 'tags', 'comment', 'click', 'like')
        fields = ('id', 'title', 'desc', 'create_time',
                  'update_time', 'author', 'click', 'like', 'category', 'istop', 'cover', 'isrecommend')
        read_only_fields = ('id', 'title', 'desc', 'create_time',
                            'update_time', 'author', 'cover',
                            'click', 'like', 'category', 'istop', 'picture', 'isrecommend')
        depth = 1


class ArticleDetailSerializer(serializers.ModelSerializer):
    # tags_label = serializers.CharField(source='tags.label', many=True)
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Article
        fields = ('title', 'content', 'create_time', 'update_time',
                  'author', 'tags', 'click', 'like', 'comment_enable', 'desc', 'isrecommend')
        read_only_fields = ('title', 'content', 'create_time', 'update_time',
                            'author', 'tags', 'click', 'like', 'comment_enable', 'desc', 'isrecommend')


class ArticleLikeSerializer(serializers.Serializer):
    like = serializers.BooleanField(required=True)
