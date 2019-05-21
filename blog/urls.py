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
from apps.article.views import ArticleListViewSet, ArticleDetailViewSet
from apps.article.views import CommentViewSet
from django.views.static import serve
from .settings import MEDIA_ROOT

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'articlelist', ArticleListViewSet, base_name='articlelist')
router.register(r'articledetail', ArticleDetailViewSet, base_name='articledetail')
router.register(r'comment', CommentViewSet)

urlpatterns = [
    url('api/', include(router.urls)),  # Api Root
    url('xadmin/', xadmin.site.urls),
    # 富文本
    url('ueditor/', include('DjangoUeditor.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root':MEDIA_ROOT})
]
