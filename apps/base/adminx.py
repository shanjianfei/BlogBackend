from .models import BlogCategory, BaseBlog
import xadmin


class BlogCategoryAdmin(object):
    list_display = ['name', 'desc', 'category', 'category_level', 'parent_category', 'create_time']
    readonly_fileds = ['create_time']


class BaseBlogAdmin(object):
    list_display = ('id', 'title', 'create_time', 'update_time', 'category', 'author', 'cover', 'tags', 'comment_enable', 'click', 'like', 'desc', 'istop', 'isrecommend')
    readonly_fileds = ['id', 'create_time']

xadmin.site.register(BlogCategory, BlogCategoryAdmin)
    
