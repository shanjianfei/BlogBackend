from django.contrib.syndication.views import Feed
from django.shortcuts import reverse
from .models import Article


class BlogFeed(Feed):
    # 标题
    title = '小黑猫的个人博客'
    # 描述
    description = '小黑猫来了，赶紧避让'
    # 链接
    link = "/rss/"

    def items(self):
        # 返回所有文章
        return Article.objects.all()

    def item_title(self, item):
        # 返回文章标题
        return item.title

    def item_description(self, item):
        # 返回文章内容
        return item.brief_introduction

    def item_link(self, item):
        # 返回文章详情页的路由
        print(item.get_absolute_url())
        return item.get_absolute_url()
