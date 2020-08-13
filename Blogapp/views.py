from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import ArticlePost
import markdown
from .forms import ArticlePostForm
from django.contrib.auth.models import User
from .models import Category
# Create your views here.
# 主页视图
def index(request):
    # 取出所有博客文章
    articles = ArticlePost.objects.all()
    # 传递给模板的对象
    context = {'articles': articles}
    return render(request, 'base/index.html', context)

# 文章详情视图
def article_detail(request, id):
    # 取出文章
    article = ArticlePost.objects.get(id=id)
    # markdown渲染
    article.body = markdown.markdown(article.body,
    extensions=[
        # 包含 缩写、表格等扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    # 传递对象给模板文件
    context = {'article' : article}
    # 返回界面
    return render(request, 'article/detail.html', context)

# 写文章视图
def article_create(request):
    # 判断用户是否提交数据
    if request.method == 'POST':
        # 将数据赋值到表单中
        article_post_form = ArticlePostForm(data=request.POST)
        # 判断提交的数据是否满足要求
        if article_post_form.is_valid():
            # 保存数据，暂时不提交到数据库
            new_article = article_post_form.save(commit=False)
            new_article.author = User.objects.get(id=1)
            if request.POST['category'] != 'none':
                new_article.category = Category.objects.get(id=request.POST['category'])
            new_article.save()
            article_post_form.save_m2m()
            return redirect("Blogapp:index")
        else:
            return HttpResponse("表单内容有误，请重新填写")
    # 如果用户请求数据
    else:
        # 创建表单实例
        article_post_form = ArticlePostForm()
        categories = Category.objects.all()
        # 赋值
        context = { 'article_post_form':article_post_form, 'categories':categories}
        # 返回模板
        return render(request, 'article/create.html', context)

# 文章归档页视图
def article_archive(request):
    articles = ArticlePost.objects.all()
    context = {'articles':articles}
    return render(request, 'archives/archives.html', context)

# 文章分类页视图
def article_category(request):
    pass