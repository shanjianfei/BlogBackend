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
from article.views import ArticleViewSet
from siteinfo.views import SiteInfoViewSet
from bloggerinfo.views import BloggerInfoViewSet

from comment.views import CommentViewSet, CommentLikeViewSet

from django.views.static import serve
from .settings import MEDIA_ROOT

from index.views import index

from article.feed import BlogFeed

from base.views import CategoryLevelViewSet, CategorySingleViewSet, TagsViewSet, BaseBlogViewSet
from user.views import UserLoginAPIView
from user.views import UserRegisterAPIView

from rest_framework import routers
import rest_framework
from rest_framework.authtoken import views

router = routers.DefaultRouter()
# router.register(r'login', LoginViewSet, base_name='login')
# router.register(r'register', RegisterViewSet, base_name='register')
router.register(r'article', ArticleViewSet, base_name='article')
# router.register(r'articlelike', ArticleLikeViewSet, base_name='articlelike')
router.register(r'tag', TagsViewSet, base_name='tag')
router.register(r'blog', BaseBlogViewSet, base_name='blog')

router.register(r'comment', CommentViewSet, base_name='comment')
router.register(r'commentlike', CommentLikeViewSet, base_name='commentlike')

router.register(r'siteinfo', SiteInfoViewSet, base_name='siteinfo')
router.register(r'bloggerinfo', BloggerInfoViewSet)
router.register(r'categorylevel', CategoryLevelViewSet,
                base_name='categorylevel')
router.register(r'singlecategory', CategorySingleViewSet,
                base_name='singlecategory')

urlpatterns = [
    url(r'^login/', UserLoginAPIView.as_view()),
    url(r'^register/', UserRegisterAPIView.as_view()),
    url('^api/', include(router.urls)),  # Api Root
    url('^xadmin/', xadmin.site.urls),
    # 富文本
    url('ueditor/', include('DjangoUeditor.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url('^api/rss/', BlogFeed(), name='rss'),
    url('^.*$', index),
    url('api-token-auth/', views.obtain_auth_token),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
