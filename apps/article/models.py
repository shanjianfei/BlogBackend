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


class ArticleCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(verbose_name='文章分类', max_length=32)

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name + '列表'

    def __str__(self):
        return self.category


class BookCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(verbose_name='书籍分类', max_length=32)

    class Meta:
        verbose_name = '书籍分类'
        verbose_name_plural = verbose_name + '列表'

    def __str__(self):
        return self.category


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
    istop_choices = (
        (True, '置顶'),
        (False, '不置顶')
    )
    isrecommend_choices = (
        (True, '推荐'),
        (False, '不推荐')
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='文章标题', null=False, blank=False, max_length=128)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    category = models.ForeignKey(ArticleCategory, verbose_name='文章分类', null=True, blank=True)
    author = models.ForeignKey(User, to_field='name', null=True, blank=True)
    picture = models.ImageField(verbose_name='头像',
                                upload_to='images/articlepicture',
                                null=True,
                                blank=True)
    tags = models.ManyToManyField(Tags, verbose_name='标签')
    comment_enable = models.BooleanField(verbose_name='是否开启评论功能', choices=comment_choices, default=True)
    click = models.IntegerField(verbose_name='点击量', default=0)
    like = models.IntegerField(verbose_name='点赞', default=0)
    content = UEditorField(toolbars="full", imagePath="images/",
                           filePath="files/", upload_settings={"imageMaxSize": 1204000},
                           settings={}, verbose_name='文章内容')
    brief_introduction = models.TextField(verbose_name='文章简介', null=True, blank=True, max_length=128)
    istop = models.BooleanField(verbose_name='置顶', choices=istop_choices, default=False)
    isrecommend = models.BooleanField(verbose_name='推荐', choices=isrecommend_choices, default=False)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name + '列表'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '{0}/{1}'.format('/article', self.id)


class Comment(models.Model):
    root_chioice = (
        (True, '是'),
        (False, '否')
    )
    top_choice = (
        (True, '是'),
        (False, '否')
    )
    id = models.AutoField(primary_key=True)
    author = models.CharField(verbose_name='评论者昵称', max_length=20)
    article = models.ForeignKey(ArticleModel, related_name='comment')
    content = models.CharField(verbose_name='评论内容', max_length=250, null=True, blank=True)
    create_time = models.DateTimeField(verbose_name='评论时间', auto_now_add=True)
    like = models.IntegerField(verbose_name='评论点赞', default=0)
    unlike = models.IntegerField(verbose_name='评论踩', default=0)
    is_root = models.BooleanField(verbose_name='评论是否是根评论', choices=root_chioice, default=True)
    is_top = models.BooleanField(verbose_name='评论是否置顶', choices=top_choice, default=False)
    super_comment = models.ForeignKey('self', verbose_name='上层评论', related_name='sub_comment', null=True, blank=True)
    belong_root = models.ForeignKey('self', verbose_name='属于哪个根目录', related_name='belong_comment', null=True, blank=True)
    sub_comment_count = models.IntegerField(verbose_name='子评论数量', default=0)

    class Meta:
        verbose_name = '文章评论'
        verbose_name_plural = verbose_name + '列表'

    def __str__(self):
        return self.content
