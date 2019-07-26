from django.db import models
from article.models import Article

# Create your models here.

class Comment(models.Model):
    root_chioice = (
        (True, '是'),
        (False, '否')
    )
    top_choice = (
        (True, '是'),
        (False, '否')
    )
    active_choice = (
        (True, '未删除'),
        (False, '已删除')
    )
    id = models.AutoField(primary_key=True)
    user = models.CharField(verbose_name='评论者昵称', max_length=20)
    article = models.ForeignKey(Article, related_name='comments')
    content = models.CharField(verbose_name='评论内容', max_length=250, null=True, blank=True)
    create_time = models.DateTimeField(verbose_name='评论时间', auto_now_add=True)
    like = models.IntegerField(verbose_name='评论点赞', default=0)
    unlike = models.IntegerField(verbose_name='评论踩', default=0)
    is_root = models.BooleanField(verbose_name='评论是否是根评论', choices=root_chioice, default=True)
    is_top = models.BooleanField(verbose_name='评论是否置顶', choices=top_choice, default=False)
    is_active = models.BooleanField(verbose_name='是否删除', choices=active_choice, default=True)
    super_comment = models.ForeignKey('self', verbose_name='上层评论', related_name='sub_comment', null=True, blank=True)
    belong_root = models.ForeignKey('self', verbose_name='属于哪个根目录', related_name='all_sub_comment', null=True, blank=True)
    sub_comment_count = models.IntegerField(verbose_name='子评论数量', default=0)

    class Meta:
        verbose_name = '文章评论'
        verbose_name_plural = verbose_name + '列表'

    def __str__(self):
        return self.content
