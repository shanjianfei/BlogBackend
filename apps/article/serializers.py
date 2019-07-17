from article.models import Article
from rest_framework import serializers


# class TagNormalSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tags
#         fields = ('label', 'color')


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
                  'author', 'tags', 'click', 'like', 'comment_enable', 'brief_introduction', 'isrecommend')
        read_only_fields = ('title', 'content', 'create_time', 'update_time',
                            'author', 'tags', 'click', 'like', 'comment_enable', 'brief_introduction', 'isrecommend')


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('user_id', 'name', 'phone', 'email', 'gender', 'avater')


# 查询每个标签下有多少article
# class TagSerializer(serializers.ModelSerializer):
#     article_count = serializers.SerializerMethodField()

#     def get_article_count(self, obj):
#         return len(obj.articlemodel_set.all())

#     class Meta:
#         model = Tags
#         fields = ('article_count', 'label', 'color')


