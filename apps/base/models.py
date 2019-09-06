import datetime
from django.db import models
from django.db.models import F
from django.conf import settings
from DjangoUeditor.models import UEditorField


# Create your models here.
AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class BaseCategory(models.Model):
    CATEGORY = (
        ('article', '文章'),
        ('book', '书籍')
    )
    name = models.CharField(verbose_name='分类别名', max_length=25)
    desc = models.TextField(verbose_name='类别描述', max_length=120, null=True, blank=True)
    category = models.CharField(verbose_name='分类', max_length=25, choices=CATEGORY, help_text='添加到头部导航')
    index = models.CharField(verbose_name="索引", max_length=120, default="index", help_text="前端导航item中的index")
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '总分类'
        verbose_name_plural = verbose_name + '列表'


class BlogCategory(models.Model):
    CATEGORY_LEVEL = (
        (1, '一级'),
        (2, '二级'),
        (3, '三级')
    )
    name = models.CharField(verbose_name='分类别名', max_length=25)
    desc = models.TextField(verbose_name='类别描述', max_length=120, null=True, blank=True)
    category = models.ForeignKey(BaseCategory, verbose_name='总分类', related_name='sub_category')
    category_level = models.IntegerField(verbose_name='分类等级', choices=CATEGORY_LEVEL, help_text='分类级别')
    parent_category = models.ForeignKey('self', verbose_name='父分类', related_name='sub_categorylevel', null=True, blank=True, help_text='父分类')
    index = models.CharField(verbose_name="索引", max_length=120, default="index", help_text="前端导航item中的index")
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name + '列表'
    
    def __str__(self):
        return self.name


class Tags(models.Model):
    COLOR_TYPE = (
        ("#878D99", "灰色"),
        ("#409EFF", "蓝色"),
        ("#67C23A", "绿色"),
        ("#EB9E05", "黄色"),
        ("#FA5555", "红色")
    )
    id = models.AutoField(primary_key=True)
    label = models.CharField(verbose_name='标签名称', max_length=32)
    description = models.CharField(verbose_name='标签描述', max_length=250, null=True, blank=True)
    color = models.CharField(verbose_name='标签颜色', max_length=20, default='#409EFF', choices=COLOR_TYPE)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name + '列表'
        # app_label = 'tag'

    def __str__(self):
        return self.label



class BaseBlog(models.Model):
    comment_choices = (
        (True, '开启评论'),
        (False, '关闭评论'),
    )
    istop_choices = (
        (True, '置顶'),
        (False, '不置顶')
    )
    isrecommend_choices = (
        (True, '推荐'),
        (False, '不推荐')
    )
    isencrypt_choices = (
        (True, '加密'),
        (False, '不加密')
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='标题', null=False, blank=False, max_length=128)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    category = models.ForeignKey(BlogCategory, verbose_name='分类', null=True, blank=True)
    author = models.ForeignKey(AUTH_USER_MODEL, null=True, blank=True)
    cover = models.ImageField(verbose_name='封面',
                                upload_to='images/cover',
                                null=True,
                                blank=True)
    tags = models.ManyToManyField(Tags, related_name='blog', verbose_name='标签')
    comment_enable = models.BooleanField(verbose_name='是否开启评论功能', choices=comment_choices, default=True)
    click = models.IntegerField(verbose_name='点击量', default=0)
    like = models.IntegerField(verbose_name='点赞', default=0)
    desc = models.TextField(verbose_name='简介', null=True, blank=True, max_length=128)
    istop = models.BooleanField(verbose_name='置顶', choices=istop_choices, default=False)
    isrecommend = models.BooleanField(verbose_name='推荐', choices=isrecommend_choices, default=False)
    isencrypt = models.BooleanField(verbose_name='博客加密', choices=isencrypt_choices, default=False)
    password = models.CharField(verbose_name='浏览博客密码', null=True, blank=True, max_length=10)

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = verbose_name + '列表'
        # app_label = 'blog'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.update_time = datetime.datetime.now()
        super().save(*args, **kwargs)
