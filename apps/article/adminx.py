from . import models

import xadmin


class ArticleModelAdmin(object):
    list_display = ('id', 'title', 'create_time', 'update_time', 'category', 'author', 'tags', 'click', 'like')
    readonly_fields = ('id', 'create_time', 'update_time', 'click', 'like')
    style_fields = {"content": "ueditor"}


class UserModelAdmin(object):
    list_display = ('name', 'phone', 'email', 'gender', 'avatar')


class CategoryModelAdmin(object):
    list_display = ['id', 'catgory']


class TagsModelAdmin(object):
    list_display = ['id', 'label', 'description', 'color']


class CommentModelAdmin(object):
    list_display = ['id', 'author', 'article', 'content', 'create_time', 'like']


xadmin.site.register(models.ArticleModel, ArticleModelAdmin)
xadmin.site.register(models.User, UserModelAdmin)
xadmin.site.register(models.Catgory, CategoryModelAdmin)
xadmin.site.register(models.Comment, CommentModelAdmin)
xadmin.site.register(models.Tags, TagsModelAdmin)
