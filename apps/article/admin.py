from django.contrib import admin

from .models import Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'create_time', 'update_time', 'click', 'like')


admin.site.register(Article, ArticleAdmin)
