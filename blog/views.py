from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.http import Http404
from django.shortcuts import render

# Create your views here.
from blog.models import Article, ArticleCategory


# 首页
# 分页页码默认设为1
def home(request, num=1):
    articles_data = Article.objects.all()  # 文章
    sidebar_category = ArticleCategory.objects.values('category').distinct().annotate(num_articles=Count('article'))
    paginator = Paginator(articles_data, 10)  # 分页，每页10个
    try:
        articles = paginator.page(num)
    except PageNotAnInteger:  # 如果接到值不为数字，如/page/xdf/
        raise Http404
    except EmptyPage:  # 如果接到的num页码数不存在，则显示最后一页
        articles = paginator.page(paginator.num_pages)
    return render(request, 'home.html', locals())


# 文章详情
def article_detail(request, year, month, id):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404
    # article = Article.objects.filter(id=article_id)[0] 约等同于上条
    # get()返回单条数据，filter返回QuerySet多条数据
    return render(request, 'detail.html', locals())


# 归档视图
def archive(request, fil):
    try:
        if fil == 'All':
            # 相当于select id,post_time,title from Article
            posts = Article.objects.only('id', 'post_time', 'title').order_by('-post_time')
        else:  # 根据传入的filter查询不同类别 select id,post_time,title from Article where category = fil
            posts = Article.objects.filter(category__category=fil)  # 多表联查，category是外键，查到该外键表里的category
        years = set()
        # 查询每篇文章的year添加到不可重复set()中
        for post in posts:
            years.add(post.post_time.year)  # 只添加年，以此类推，month,day
        # years转换成list并降序排序
        years = list(years)
        years.sort(reverse=True)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'archive.html', locals())


# 分类详情
def category_by_name(request):
    try:
        category = ArticleCategory.objects.values('category').distinct().order_by('category')  # 装入的是Article对象
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'category_by_name.html', locals())


def search_by_title_or_content(request):
    # sw = request.GET['sw']  # 注意，此处是[]
    sw = request.GET.get('sw')  # 注意，此处是()
    if not sw:
        error = True
        home(request, 1)
    else:
        data = Article.objects.only('id', 'post_time', 'title', 'content')
        result = set()
        # 循环对象匹配结果
        for x in data:
            if sw in x.title:
                result.add(x)
            elif sw in x.content:
                result.add(x)
        count = len(result)
        error = True if count == 0 else False
    return render(request, 'search.html', locals())


def collections(request):
    try:
        coll_tag = ArticleCategory.objects.get(category='collection')
        collection = coll_tag.article_set.all().order_by('post_time')
    except ArticleCategory.DoesNotExist:
        raise Http404
    return render(request, 'collection.html', locals())


def about_me(request):
    return render(request, 'about_me.html', locals())


def ex(request):
    return render(request, 'examples.html', locals())
