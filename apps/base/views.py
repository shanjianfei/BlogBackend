from django.shortcuts import render
from rest_framework import viewsets, mixins, filters, status
from rest_framework import pagination
from rest_framework.response import Response
from django_filters import rest_framework

from django.db.models import F
from .models import BaseCategory, BlogCategory, Tags, BaseBlog
from .serializers import BaseCategorySerializer, CategoryLevelSerializer, TagsSerializer, BaseBlogSerialzier, BaseBlogReadPermissionVerificationSerializer

# Create your views here.

class CategorySingleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogCategory.objects.filter(category_level=1)
    serializer_class = CategoryLevelSerializer


# 获取总分类
class CategoryLevelViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = BaseCategorySerializer
    queryset = BaseCategory.objects.all()


class TagsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TagsSerializer
    queryset = Tags.objects.all()


class BaseBlogViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = BaseBlog.objects.all()
    serializer_class = BaseBlogSerialzier
    filter_backends = (rest_framework.DjangoFilterBackend, filters.OrderingFilter)
    ordering_field = ('create_time', 'click')
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.isencrypt:
            password = request.data.get('password', None)
            if password is None:
                return Response(data={'result': '需要密码' }, status=status.HTTP_400_BAD_REQUEST)
            else:
                if instance.password == password:
                    return Response(status=status.HTTP_200_OK, data={'msg': '验证通过'})
                else:
                    return Response(data={'result': '密码错误'}, status=status.HTTP_400_BAD_REQUEST)
        instance.click = F('click') + 1
        instance.save()
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class VerifyBlogPasswordViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = BaseBlogReadPermissionVerificationSerializer
    queryset = BaseBlog.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True) # 出错返回400
        blog_id = serializer.validated_data['blog_id']
        psd_post = serializer.validated_data['password']
        objs = self.queryset.filter(id=blog_id)
        if len(objs):
            # if not objs[0].isencrypt:
            #     return Response(data=data, status=status.HTTP_200_OK)
            if objs[0].password == psd_post:
                data = {'result': 'success', 'msg': '验证通过'}
            else:
                data = {'result': 'success', 'msg': '验证失败'}
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            return Response(data={'result': 'fail', 'msg': '文章不存在'}, status=status.HTTP_404_NOT_FOUND)

        
