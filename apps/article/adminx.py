from . import models

import xadmin


class ArticleAdmin(object):
    list_display = ('id', 'title', 'create_time', 'update_time', 'category', 'author', 'tags', 'click', 'like')
    readonly_fields = ('id', 'create_time', 'update_time', 'click', 'like')
    style_fields = {"content": "ueditor"}

xadmin.site.register(models.Article, ArticleAdmin)
