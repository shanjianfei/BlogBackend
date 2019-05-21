from rest_framework import viewsets, status, mixins, filters
from rest_framework.response import Response
from .serializers import ArticleListSerializer, UserSerializer, CommentSerializer, ArticleDetailSerializer
from .models import ArticleModel, User, Comment
from django_filters import rest_framework
from .filters import ArticleListFilter, CommentFilter
from rest_framework.pagination import PageNumberPagination

# Create your views here.


class ArticleListPagination(PageNumberPagination):
    page_size = 2
    max_page_size = 3
    page_size_query_param = 'size'
    page_query_param = 'page'


class ArticleListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = ArticleModel.objects.all()
    serializer_class = ArticleListSerializer
    pagination_class = ArticleListPagination

    # 分别对应 过滤、搜索、排序
    filter_backends = (rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_class = ArticleListFilter
    filter_fields = ('title', 'category', 'min_datetime', 'max_datetime')
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


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (rest_framework.DjangoFilterBackend, filters.OrderingFilter)
    filter_class = CommentFilter
    ordering = ('-create_time',)
