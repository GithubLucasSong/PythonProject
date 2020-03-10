from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=32, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=128, verbose_name='密码')
    position = models.CharField(max_length=32, verbose_name='职位')
    company = models.CharField(
        blank=True,
        max_length=32,
        choices=(('1', '北京总公司'), ('2', '上海分公司'), ('3', '广州分公司')),
        verbose_name='公司')
    # company = models.CharField(max_length=32,verbose_name='公司')
    phone = models.CharField(max_length=11, verbose_name='手机号')
    last_login_time = models.DateTimeField(null=True, blank=True, verbose_name='上次登录时间')
    register_time = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')
    is_active = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='img/avatar',default='img/avatar/default.jpeg')


    def __str__(self):
        return self.username


class Category(models.Model):
    # 文章标题
    title = models.CharField(max_length=64, verbose_name='板块标题')

    def __str__(self):
        return self.title


class Article(models.Model):
    '''
    标题 文章摘要 发表的时间 作者 板块 创建时间 更新时间 删除状态
    '''
    title = models.CharField(max_length=32, verbose_name='文章标题')
    abstract = models.CharField(max_length=256, verbose_name='文章摘要')
    author = models.ForeignKey('User', on_delete=models.DO_NOTHING, null=True, verbose_name='作者')
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='分类')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    publish_status = models.BooleanField(default=False, choices=((False, '未发布'), (True, '已发布')), verbose_name='发布状态')
    detail = models.OneToOneField(to='ArticleDetail', on_delete=models.DO_NOTHING, verbose_name='文章内容')

    def show_publish_status(self):
        color_dict = {True: 'green', False: 'red'}
        return '<span style="background: {};color: white;padding: 3px">{}</span>'.format(
            color_dict[self.publish_status], self.get_publish_status_display())

from ckeditor_uploader.fields import RichTextUploadingField
class ArticleDetail(models.Model):
    content = RichTextUploadingField(verbose_name='文章内容')


class Comment(models.Model):
    '''
    评论表
    评论者 评论内容 评论文章 时间 审核状态
    '''
    author = models.ForeignKey(verbose_name='评论者', to='User', on_delete=models.DO_NOTHING)
    content = models.TextField(verbose_name='评论内容')
    article = models.ForeignKey(verbose_name='文章', to='Article', on_delete=models.DO_NOTHING)
    time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    status = models.BooleanField(verbose_name='审核状态', default=True)
