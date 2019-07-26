from rest_framework import viewsets, status, mixins, filters
from rest_framework.response import Response
from .serializers import ArticleSerializer, ArticleDetailSerializer, ArticleLikeSerializer
from article.models import Article
from django_filters import rest_framework
from .filters import ArticleListFilter
from rest_framework.pagination import PageNumberPagination

from django.db.models import F

# Create your views here.


class ArticlePagination(PageNumberPagination):
    page_size = 6
    max_page_size = 10
    page_size_query_param = 'size'
    page_query_param = 'page'

    def get_next_link(self):
        if not self.page.has_next():
            return None
        page_number = self.page.next_page_number()
        return page_number

class ArticleViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Article.objects.all()
    pagination_class = ArticlePagination

    # 分别对应 过滤、搜索、排序
    filter_backends = (rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_class = ArticleListFilter
    search_fields = ('^category__name',)
    ordering_fields = ('update_time', 'click')

    def get_serializer_class(self):
        if self.action == 'update':
            return ArticleLikeSerializer
        elif self.action == 'retrieve':
            return ArticleDetailSerializer
        else:
            return ArticleSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click = F('click') + 1
        instance.save()
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        if 'like' in request.data:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            like = serializer.validated_data['like']
            instance = self.get_object()
            if like:
                instance.like = F('like') + 1
                instance.save()
                return Response(data={'result': '点赞成功'}, status=status.HTTP_200_OK)
        else:
            return Response(data={'result': '参数错误'}, status=status.HTTP_400_BAD_REQUEST)
