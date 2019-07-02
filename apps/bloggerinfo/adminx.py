from .models import BloggerInfo, Social
import xadmin


class SocialShip(object):
    model = BloggerInfo.social.through
    extra = 1


class SocialAdmin(object):
    list_display = ('name', 'desc', 'url', 'image')
    readonly_fields = ('image_height', 'image_width')


class BloggerInfoAdmin(object):
    list_display = ('name_zh', 'name_en', 'intro', 'email', 'phone_number', 'avatar', 'social')
    exclude = ['social', ]
    inlines = [SocialShip,]


xadmin.site.register(BloggerInfo, BloggerInfoAdmin)
xadmin.site.register(Social, SocialAdmin)
