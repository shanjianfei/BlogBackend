from django.db import models

# Create your models here.


class Social(models.Model):
    name = models.CharField(verbose_name='社交平台名称', max_length=20)
    desc = models.TextField(verbose_name='描述', null=True, blank=True, max_length=120)
    url = models.CharField(verbose_name='网址', max_length=120, null=True, blank=True)
    image = models.ImageField(verbose_name='图片', height_field='image_height', width_field='image_width', upload_to='images/social', null=True, blank=True)
    image_height = models.IntegerField(verbose_name='图片高度', null=True, blank=True)
    image_width = models.IntegerField(verbose_name='图片宽度', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '社交平台'
        verbose_name_plural = verbose_name + '列表'

class BloggerInfo(models.Model):
    name_zh = models.CharField(verbose_name='中文名', null=True, blank=True, max_length=20)
    name_en = models.CharField(verbose_name='英文名', null=True, blank=True, max_length=20)
    intro = models.TextField(verbose_name='简介',null=True, blank=True, max_length=120)
    email = models.EmailField(verbose_name='电子邮箱',null=True, blank=True)
    phone_number = models.CharField(verbose_name='手机号码', null=True, blank=True, max_length=11)
    avatar = models.ImageField(verbose_name='头像', null=True, blank=True, upload_to='images/avatar')
    background = models.ImageField(verbose_name='背景', upload_to='images/background', default='images/background/background.jpeg', null=True, blank=True,)
    social = models.ManyToManyField(Social, verbose_name='社交平台', null=True, blank=True,)

    def __str__(self):
        return self.name_zh

    class Meta:
        verbose_name = '博主信息'
        verbose_name_plural = verbose_name
