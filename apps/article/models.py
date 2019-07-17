from django.db import models
from base.models import BaseBlog
from DjangoUeditor.models import UEditorField


# Create your models here.


class Article(BaseBlog):
    content = UEditorField(toolbars="full", imagePath="images/",
                           filePath="files/", upload_settings={"imageMaxSize": 1204000},
                           settings={}, verbose_name='文章内容')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name + '列表'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '{0}/{1}'.format('/article', self.id)
