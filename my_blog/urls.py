"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from blog import views

urlpatterns = [

    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/p/(?P<id>\d+)/$',
        views.article_detail, name='articleDetail'),    # 文章详情
    url(r'^archive/(?P<fil>\w+)/$', views.archive, name='archive'),  # 文章分类结果
    url(r'^category/$', views.category_by_name, name='category'),   # 文章全部分类
    url(r'^search/$', views.search_by_title_or_content, name='search'),
    url(r'^about_me$', views.about_me, name='aboutMe')


]
