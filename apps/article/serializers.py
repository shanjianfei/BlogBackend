from rest_framework import serializers
from .models import ArticleModel, User, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('author', 'article', 'content', 'create_time', 'like')


class ArticleListSerializer(serializers.ModelSerializer):
    comment = len(CommentSerializer(many=True).data)
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = ArticleModel
        # fields = ('title', 'content', 'create_time', 'update_time',
        # 'catgory', 'author', 'picture', 'tags', 'comment', 'click', 'like')
        fields = ('id', 'title', 'brief_introduction', 'create_time',
                  'update_time', 'author', 'picture', 'comment', 'tags', 'click', 'like', 'category')
        read_only_fields = ('id', 'title', 'brief_introduction', 'create_time',
                            'update_time', 'author', 'picture', 'comment', 'tags,' 'click', 'like', 'category')


class ArticleDetailSerializer(serializers.ModelSerializer):
    # tags_label = serializers.CharField(source='tags.label', many=True)
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = ArticleModel
        fields = ('title', 'content', 'create_time', 'update_time', 'author', 'tags', 'click', 'like', 'comment_enable')
        read_only_fields = ('title', 'content', 'create_time', 'update_time', 'author', 'tags', 'click', 'like', 'comment_enable')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'name', 'phone', 'email', 'gender', 'avater')


