from django.http import Http404
from django.shortcuts import render

# Create your views here.
from blog.models import Article


def home(request):
    articles = Article.objects.all()
    return render(request, 'home.html', locals())


def article_detail(request, year, month, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404
    # article = Article.objects.filter(id=article_id)[0] 约等同于上条
    # get()返回单条数据，filter返回QuerySet多条数据
    return render(request, "detail.html", locals())
