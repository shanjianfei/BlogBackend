from rest_framework import viewsets, status, mixins, filters
from rest_framework.response import Response
from .serializers import ArticleListSerializer, UserSerializer,\
    CommentSerializer, ArticleDetailSerializer, TagSerializer,\
    ArticleCategorySerializer, SubCommentSerializer, CommentLikeSerializer,\
    SubCommentLenSerializer
from .models import ArticleModel, User, Comment, Tags, ArticleCategory
from django_filters import rest_framework
from .filters import ArticleListFilter, CommentFilter
from rest_framework.pagination import PageNumberPagination

# Create your views here.


class ArticleListPagination(PageNumberPagination):
    page_size = 6
    max_page_size = 10
    page_size_query_param = 'size'
    page_query_param = 'page'

    def get_next_link(self):
        if not self.page.has_next():
            return None
        page_number = self.page.next_page_number()
        print(self.page_query_param)
        return page_number

class ArticleListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = ArticleModel.objects.all()
    serializer_class = ArticleListSerializer
    pagination_class = ArticleListPagination

    # 分别对应 过滤、搜索、排序
    filter_backends = (rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_class = ArticleListFilter
    filter_fields = ('title', 'category', 'min_datetime', 'max_datetime', 'tags', 'isrecommend')
    # search_fields = ('^category__catgory')
    ordering_fields = ('update_time', 'click')


class ArticleDetailViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = ArticleModel.objects.all()
    serializer_class = ArticleDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if 'like' in request.data:
            if type(request.data['like']) == bool and request.data['like']:
                instance.like += 1
                instance.save()
                serializer = self.get_serializer(instance)
                return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CommentViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    filter_backends = (rest_framework.DjangoFilterBackend, filters.OrderingFilter)
    filter_class = CommentFilter
    filter_fields = ('article',)
    ordering = ('-create_time',)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        is_root = serializer.validated_data['is_root']
        if not is_root: # 不是根评论
            # 如果不是根评论， 下面的两个属性一定要有
            super_comment = serializer.validated_data.get('super_comment', '') # 上层评论
            belong_root = serializer.validated_data.get('belong_root', '') # 当前评论所属的根评论
            print(belong_root)
            if super_comment and belong_root:
                instance_root = Comment.objects.filter(id=belong_root.id)
                if instance_root and instance_root[0].is_root: # 判断上传的root comment id 对应的是否是root comment
                    instance_root[0].sub_comment_count += 1
                    instance_root[0].save()
                    self.perform_create(serializer)
                    return Response(status=status.HTTP_201_CREATED, data={'result': '添加评论成功'})
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else: # 根评论
            self.perform_create(serializer)
            return Response(status=status.HTTP_201_CREATED, data={'result': '添加评论成功'})

    def get_queryset(self):
        return Comment.objects.filter(is_root=True)


    def get_serializer_class(self):
        if self.action == 'list':
            return SubCommentSerializer
        elif self.action == 'retrieve':
            return SubCommentSerializer
        else:
            return CommentSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer


class ArticleCategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = ArticleCategory.objects.all()
    serializer_class = ArticleCategorySerializer
