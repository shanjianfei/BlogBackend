from . import models

import xadmin


class ArticleAdmin(object):
    list_display = ('id', 'title', 'create_time', 'update_time', 'category', 'author', 'tags', 'click', 'like', 'isencrypt')
    readonly_fields = ('id', 'click', 'like')
    style_fields = {"content": "ueditor"}

xadmin.site.register(models.Article, ArticleAdmin)
