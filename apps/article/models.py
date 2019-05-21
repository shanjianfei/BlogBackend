from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.


class User(models.Model):
    gender_choice = (
        ('0', 'female'),
        ('1', 'male')
    )
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='名字', max_length=32, unique=True)
    phone = models.CharField(verbose_name='手机号码', max_length=11, null=True, blank=True)
    email = models.CharField(verbose_name='邮箱', null=True, blank=True, max_length=60)
    gender = models.CharField(verbose_name='性别', null=True, blank=True, choices=gender_choice, max_length=2)
    avatar = models.ImageField(verbose_name='头像', null=True, blank=True,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name + '列表'


class Catgory(models.Model):
    id = models.AutoField(primary_key=True)
    catgory = models.CharField(verbose_name='文章分类', max_length=32, help_text='目前支持前端，后端两种分类')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name + '列表'

    def __str__(self):
        return self.catgory


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

    def __str__(self):
        return self.label


class ArticleModel(models.Model):
    comment_choices = (
        (True, '开启评论'),
        (False, '关闭评论'),
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='文章标题', null=False, blank=False, max_length=128)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    category = models.ForeignKey(Catgory, verbose_name='文章分类', null=True, blank=True)
    author = models.ForeignKey(User, to_field='name', null=True, blank=True)
    picture = models.ImageField(verbose_name='头像',
                                upload_to='images/articlepicture',
                                null=True,
                                blank=True)
    tags = models.ManyToManyField(Tags, verbose_name='标签')
    comment_enable = models.BooleanField(verbose_name='是否开启评论功能', choices=comment_choices, default=True)
    # comment = models.TextField(verbose_name='文章评论', null=True, blank=True)
    click = models.IntegerField(verbose_name='点击量', default=0)
    like = models.IntegerField(verbose_name='点赞', default=0)
    content = UEditorField(toolbars="full", imagePath="images/",
                           filePath="files/", upload_settings={"imageMaxSize": 1204000},
                           settings={}, verbose_name='文章内容')
    brief_introduction = models.TextField(verbose_name='文章简介', null=True, blank=True, max_length=128)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name + '列表'

    def __str__(self):
        return self.title


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(verbose_name='评论者昵称', max_length=20)
    article = models.ForeignKey(ArticleModel, related_name='comment')
    content = models.CharField(verbose_name='评论内容', max_length=250, null=True, blank=True)
    create_time = models.DateTimeField(verbose_name='评论时间', auto_now_add=True)
    like = models.IntegerField(verbose_name='评论点赞', default=0)

    class Meta:
        verbose_name = '文章评论'
        verbose_name_plural = verbose_name + '列表'

    def __str__(self):
        return self.content
