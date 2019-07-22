from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('id', 'like', 'unlike', 'create_time', 'is_top', 'sub_comment_count')


class SubCommentSerializer(serializers.ModelSerializer):
    """
    子评论以list显示出来
    """
    article = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        depth = 1


# 评论点赞
class CommentLikeSerializer(serializers.Serializer):
    # comment_id = serializers.IntegerField(required=True, label='评论id')
    like = serializers.BooleanField(required=True, label='喜欢或者不喜欢') # true 为 like false 为 unlike
    # like1 = serializers.CharField(required=True, max_length=120)