from django.db import models

# Create your models here.


class SiteInfoModel(models.Model):
    logo = models.ImageField(verbose_name='logo', upload_to='images/logo')
    motto = models.CharField(verbose_name='座右铭', max_length=20)
    filing = models.CharField(verbose_name='备案', max_length=20)
    copyright = models.CharField(verbose_name='版权', max_length=20)
    open_source_license = models.CharField(verbose_name='开源协议', max_length=20)
    url_osl = models.CharField(verbose_name='开源协议网站', max_length=120, blank=True, null=True)

    def __str__(self):
        return '站点信息'

    class Meta:
        verbose_name = '站点信息'
        verbose_name_plural = verbose_name
