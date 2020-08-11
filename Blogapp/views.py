from django.http import HttpResponse
from django.shortcuts import render
from .models import ArticlePost

# Create your views here.
def index(request):
    # 取出所有博客文章
    articles = ArticlePost.objects.all()
    # 传递给模板的对象
    context = {'articles': articles}
    return render(request, 'base/index.html', context)