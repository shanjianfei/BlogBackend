from rest_framework import viewsets, status, mixins, filters
from rest_framework.response import Response
from .serializers import ArticleListSerializer, ArticleDetailSerializer
from article.models import Article
from django_filters import rest_framework
from .filters import ArticleListFilter
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
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    pagination_class = ArticleListPagination

    # 分别对应 过滤、搜索、排序
    filter_backends = (rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_class = ArticleListFilter
    # filter_fields = ('title', 'category', 'min_datetime', 'max_datetime', 'tags', 'isrecommend')
    search_fields = ('^category__name',)
    ordering_fields = ('update_time', 'click')


class ArticleDetailViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Article.objects.all()
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


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class TagViewSet(viewsets.ModelViewSet):
#     queryset = Tags.objects.all()
#     serializer_class = TagSerializer
