from django.db import models
from django.contrib.auth.models import User     

# Create your models here.


class Person(User):
    gender_choice = (
        (0, 'female'),
        (1, 'male')
    )
    phone = models.CharField(verbose_name='手机号码', max_length=11, null=True, blank=True)
    gender = models.IntegerField(verbose_name='性别', choices=gender_choice, null=True, blank=True)
    avater = models.ImageField(verbose_name='头像', upload_to='avater', null=True, blank=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        abstract = True
        ordering = ['username'] # 排序


class AuthorProfile(Person):

    def __str__(self):
        return self.username

    class Meta(Person.Meta):
        verbose_name = '作者'
        verbose_name_plural = verbose_name + '列表'
        


class UserProfile(Person):
    last_login_time = models.DateTimeField(verbose_name='上次登录时间时间')

    def __str__(self):
        return self.username

    class Meta(Person.Meta):
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name + '列表'
