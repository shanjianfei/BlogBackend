from django.shortcuts import render
from rest_framework import mixins, viewsets, status, pagination
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import CommentLikeSerializer, CommentSerializer, SubCommentSerializer
from .models import Comment
from .filter import CommentFilter

# Create your views here.


class CommentPagination(pagination.PageNumberPagination):
    page_size = 10
    max_page_size = 20
    page_query_param = 'page'
    page_size_query_param = 'size'


class CommentLikeViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CommentLikeSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        comment_id = serializer.validated_data['comment_id']
        like = serializer.validated_data['like']
        instance = Comment.objects.filter(id=comment_id)
        if instance:
            _instance = instance[0]
            if like:
                _instance.like += 1
            else:
                _instance.unlike += 1
            _instance.save()
            return Response(status=status.HTTP_200_OK, data={'result': '操作成功'})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'result': '评论不存在'})


class CommentViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    pagination_class = CommentPagination
    filter_class = CommentFilter
    # filter_fields = ('article',)
    ordering = ('-create_time',)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        is_root = serializer.validated_data['is_root']
        if not is_root: # 不是根评论
            # 如果不是根评论， 下面的三个属性一定要有
            super_comment = serializer.validated_data.get('super_comment') # 上层评论
            if not super_comment:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'result': '评论已被删除'})
            belong_root = serializer.validated_data.get('belong_root') # 当前评论所属的根评论
            article = serializer.validated_data['article']
            if super_comment and \
                belong_root and \
                (article.id == belong_root.article.id) and \
                ((super_comment.belong_root == belong_root.id) or (super_comment.id == belong_root.id)):
                return Response(status=status.HTTP_201_CREATED, data={'result': '添加评论成功'})
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else: # 根评论
            article = serializer.validated_data['article']
            self.perform_create(serializer)
            return Response(status=status.HTTP_201_CREATED, data={'result': '添加评论成功'})

    def get_serializer_class(self):
        if self.action == 'list':
            return SubCommentSerializer
        elif self.action == 'retrieve':
            return SubCommentSerializer
        else:
            return CommentSerializer
