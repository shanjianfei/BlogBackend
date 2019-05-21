from django.contrib import admin

from .models import ArticleModel

# Register your models here.


class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'create_time', 'update_time', 'click', 'like')


admin.site.register(ArticleModel, ArticleModelAdmin)
