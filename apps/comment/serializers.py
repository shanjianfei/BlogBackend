from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # fields = ('id', 'author', 'article', 'content', 'create_time', 'like', 'unlike', 'sub_comment_count',
        #           'is_root', 'is_top', 'super_comment', 'belong_root')
        fields = '__all__'
        read_only_fields = ('id', 'like', 'unlike', 'create_time', 'is_top', 'sub_comment_count')


class SubCommentSerializer(serializers.ModelSerializer):
    """
    子评论以list显示出来
    """
    subs = CommentSerializer(many=True, read_only=True, source='belong_comment') # 所有子评论
    article = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Comment
        # fields = ('id', 'author', 'content', 'create_time', 'like', 'unlike', 'is_root', 'is_top', 'subs')
        fields = '__all__'
        depth = 1


class SubCommentLenSerializer(serializers.ModelSerializer):
    """
    sub_comment_count: 子评论只显示条数
    """
    sub_comment_count = serializers.SerializerMethodField()

    def get_sub_comment_count(self, comment):
        return len(Comment.objects.filter(super_comment__id=comment.id))

    class Meta:
        model = Comment
        fields = ('id', 'author', 'content', 'create_time', 'like', 'unlike', 'is_root', 'is_top', 'sub_comment_count')


# 评论点赞
class CommentLikeSerializer(serializers.Serializer):
    comment_id = serializers.IntegerField(required=True, label='评论id')
    like = serializers.BooleanField(required=True, label='喜欢或者不喜欢') # true 为 like false 为 unlike