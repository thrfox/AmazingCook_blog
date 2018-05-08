from django.db import models

# 创建数据库表

# 用户表
from django.utils import timezone
from markdownx.models import MarkdownxField


class Users(models.Model):
    user_name = models.CharField(max_length=12, unique=True, verbose_name='用户名')  # 用户名，唯一
    user_password = models.CharField(max_length=20, verbose_name='密码')
    nickname = models.CharField(max_length=20, unique=True, verbose_name='昵称')  # 用户昵称，唯一
    user_type = models.PositiveSmallIntegerField(verbose_name='用户类型')  # 用户类型

    # 用来给admin模块显示用户类型
    def user_type_format(self):
        if self.user_type == 0:
            return '超级VIP'
        elif self.user_type == 1:
            return '普通用户'

    user_type_format.short_description = '用户类型'

    def __str__(self):
        return self.nickname

    class Meta:
        ordering = ['id', ]
        verbose_name_plural = '用户'


# 类别表
class ArticleCategory(models.Model):
    category = models.CharField(max_length=30, verbose_name='类别')

    # 返回显示的字段
    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = '文章类别'


# 标签表
class ArticleTag(models.Model):
    tag = models.CharField(max_length=30, verbose_name='标签')

    # 返回显示的字段
    def __str__(self):
        return self.tag

    class Meta:
        verbose_name_plural = '标签'


# 文章表
class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')  # 标题
    # author = models.ForeignKey(Users, verbose_name='作者')  # 作者, 默认值为用户名
    category = models.ForeignKey(ArticleCategory, verbose_name='文章类别')  # 文章类别，选项选择
    tag = models.ManyToManyField(ArticleTag, max_length=50, verbose_name='标签')
    content = MarkdownxField(blank=True, null=True, verbose_name='正文')  # 文章正文，可为空，富表单
    post_time = models.DateTimeField(default=timezone.now, verbose_name='发表时间')  # 文章发表日期
    modify_time = models.DateTimeField(default=timezone.now, verbose_name='最近修改时间')  # 最近修改时间

    # 避免后台正文显示过长
    def content_format(self):
        # 如果len()>100 返回[0:100]，否则self.content
        return self.content[0:100] if len(self.content) > 100 else self.content

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-post_time']
        verbose_name_plural = '文章'  # 显示名称
