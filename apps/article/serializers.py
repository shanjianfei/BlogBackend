from rest_framework import serializers
from .models import ArticleModel, User, Comment, Tags, ArticleCategory


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'article', 'content', 'create_time', 'like', 'unlike', 'sub_comment_count',
                  'is_root', 'is_top', 'super_comment', 'belong_root')
        read_only_fields = ('id', 'like', 'unlike', 'sub_comment_count', 'create_time', 'is_top')


class SubCommentSerializer(serializers.ModelSerializer):
    subs = CommentSerializer(many=True, read_only=True, source='belong_comment') # 所有子评论
    class Meta:
        model = Comment
        fields = ('id', 'author', 'content', 'create_time', 'like', 'unlike', 'is_root', 'is_top', 'subs')


class SubCommentLenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'content', 'create_time', 'like', 'unlike', 'is_root', 'is_top', 'sub_comment_count')


# 评论点赞
class CommentLikeSerializer(serializers.Serializer):
    comment_id = serializers.IntegerField(required=True, label='评论id')
    like = serializers.BooleanField(required=True, label='喜欢或者不喜欢') # true 为 like false 为 unlike


class ArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = ('id', 'category')


class TagNormalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('label', 'color')


class ArticleListSerializer(serializers.ModelSerializer):
    comment = len(CommentSerializer(many=True).data)
    tags = TagNormalSerializer(many=True)

    class Meta:
        model = ArticleModel
        # fields = ('title', 'content', 'create_time', 'update_time',
        # 'catgory', 'author', 'picture', 'tags', 'comment', 'click', 'like')
        fields = ('id', 'title', 'brief_introduction', 'create_time',
                  'update_time', 'author', 'comment', 'tags', 'click', 'like', 'category', 'istop', 'picture', 'isrecommend')
        read_only_fields = ('id', 'title', 'brief_introduction', 'create_time',
                            'update_time', 'author', 'picture', 'comment', 'tags',
                            'click', 'like', 'category', 'istop', 'picture', 'isrecommend')


class ArticleDetailSerializer(serializers.ModelSerializer):
    # tags_label = serializers.CharField(source='tags.label', many=True)
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = ArticleModel
        fields = ('title', 'content', 'create_time', 'update_time',
                  'author', 'tags', 'click', 'like', 'comment_enable', 'brief_introduction', 'isrecommend')
        read_only_fields = ('title', 'content', 'create_time', 'update_time',
                            'author', 'tags', 'click', 'like', 'comment_enable', 'brief_introduction', 'isrecommend')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'name', 'phone', 'email', 'gender', 'avater')


# 查询每个标签下有多少article
class TagSerializer(serializers.ModelSerializer):
    article_count = serializers.SerializerMethodField()

    def get_article_count(self, obj):
        return len(obj.articlemodel_set.all())

    class Meta:
        model = Tags
        fields = ('article_count', 'label', 'color')


