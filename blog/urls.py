"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.conf.urls import url, include
from article.views import ArticleListViewSet, ArticleDetailViewSet
from siteinfo.views import SiteInfoViewSet
from bloggerinfo.views import BloggerInfoViewSet

from comment.views import CommentViewSet, CommentLikeViewSet, CommentsViewsets

from django.views.static import serve
from .settings import MEDIA_ROOT

from index.views import index

from article.feed import BlogFeed

from base.views import CategoryViewSet
from base.views import CategorysViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'articlelist', ArticleListViewSet, base_name='articlelist')
router.register(r'articledetail', ArticleDetailViewSet, base_name='articledetail')
# router.register(r'taglist', TagViewSet, base_name='taglist')
router.register(r'comment', CommentViewSet, base_name='comment')
router.register(r'commentlike', CommentLikeViewSet, base_name='commentlike')
router.register(r'comments', CommentsViewsets, base_name='comments')

router.register(r'siteinfo', SiteInfoViewSet)
router.register(r'bloggerinfo', BloggerInfoViewSet)
router.register(r'allcategory', CategoryViewSet, base_name='allcategory')
router.register(r'allcategorys', CategorysViewSet, base_name='allcategorys')

urlpatterns = [
    url('^api/', include(router.urls)),  # Api Root
    url('^xadmin/', xadmin.site.urls),
    # 富文本
    url('ueditor/', include('DjangoUeditor.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url('^api/rss/', BlogFeed(), name='rss'),
    url('^.*$', index),
]
