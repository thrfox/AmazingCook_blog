from ckeditor import fields
from django.db import models

# 创建数据库表

# 用户表
from django_markdown.models import MarkdownField


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


# 文章表
class Article(models.Model):
    CATEGORY = (
        ('Python', 'Python'),
        ('Java', 'Java'),
        ('C', 'C'),
        ('Other', 'Other'),
    )

    title = models.CharField(max_length=100, verbose_name='标题')  # 标题
    # author = models.ForeignKey(Users, verbose_name='作者')  # 作者, 默认值为用户名
    category = models.CharField(max_length=30, choices=CATEGORY, verbose_name='类别')  # 文章类别，选项选择
    post_time = models.DateTimeField(auto_now_add=True, verbose_name='发表时间')  # 文章发表日期
    modify_time = models.DateTimeField(auto_now=True, verbose_name='最近更新')  # 文章修改日期
    content = MarkdownField(blank=True, null=True, verbose_name='正文')  # 文章正文，可为空，富表单

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-post_time']
        verbose_name_plural = '文章'  # 显示名称
