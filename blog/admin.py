from django.contrib import admin
# Register your models here.
from markdownx.admin import MarkdownxModelAdmin

from blog.models import Article, Users, ArticleCategory


@admin.register(Users)  # 注册装饰器
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'user_password', 'nickname', 'user_type_format',)
    fields = ('user_name', 'user_password', 'nickname', 'user_type',)


@admin.register(Article)
class ArticleAdmin(MarkdownxModelAdmin):
    # 展示浏览框
    list_display = ('title', 'category', 'post_time', 'content_format',)  # 列表显示
    search_fields = ('title', 'category',)  # 可以用来搜索的字段
    list_filter = ('category',)  # 列表过滤
    date_hierarchy = 'post_time'  # 日期层
    ordering = ('-modify_time',)  # 按修改时间降序排列

    # 编辑框
    fields = ('title', 'category', 'content', 'post_time', 'modify_time')  # 显示被编辑的字段


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)

    fields = ('category',)
