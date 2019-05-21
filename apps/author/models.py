from django.db import models

# Create your models here.


class AuthorModel(models.Model):
    gender_choice = (
        (0, 'female'),
        (1, 'male')
    )
    name = models.CharField(verbose_name='姓名', max_length=128, null=True, blank=True)
    age = models.IntegerField(verbose_name='年龄', null=True, blank=True)
    phone = models.CharField(verbose_name='手机号码', max_length=11, null=True, blank=True)
    email = models.EmailField(verbose_name='电子邮箱', max_length=128, null=True, blank=True)
    gender = models.IntegerField(verbose_name='性别', choices=gender_choice, null=True, blank=True)
    avater = models.ImageField(verbose_name='头像',upload_to='avater')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '作者'
        verbose_name_plural = verbose_name + '列表'
