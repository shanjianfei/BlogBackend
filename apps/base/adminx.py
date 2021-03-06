from .models import BaseCategory, BlogCategory, BaseBlog, Tags
import xadmin


class BaseCategoryAdmin(object):
    list_display = ['name', 'desc', 'category', 'create_time']
    readonly_fileds = ['create_time']


class BlogCategoryAdmin(object):
    list_display = ['name', 'desc', 'category', 'category_level', 'parent_category', 'create_time']
    readonly_fileds = ['create_time']


class BaseBlogAdmin(object):
    list_display = ('id', 'title', 'create_time', 'update_time', 'category', 'author', 'cover', 'tags', 'comment_enable', 'click', 'like', 'desc', 'istop', 'isrecommend', 'isencrypt')
    readonly_fileds = ['id', 'create_time']


class TagsAdmin(object):
    list_display = ['id', 'label', 'description', 'color']
    readonly_fileds = ['id']

xadmin.site.register(BlogCategory, BlogCategoryAdmin)
xadmin.site.register(BaseCategory, BaseCategoryAdmin)
xadmin.site.register(BaseBlog, BaseBlogAdmin)
xadmin.site.register(Tags, TagsAdmin)
