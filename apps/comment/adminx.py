import xadmin
from . import models


class CommentAdmin(object):
    list_display = ['id', 'author', 'article', 'content', 'create_time', 'like', 'unlike', 'is_top', 'is_root', 'super_comment', 'belong_root', 'sub_comment_count']
    readonly_fields = ['id', 'create_time']
    style_fields = {"content": "ueditor"}

xadmin.site.register(models.Comment, CommentAdmin)
