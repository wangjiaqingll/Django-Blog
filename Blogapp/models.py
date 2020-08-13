from django.db import models
# 导入内建的User模型
from django.contrib.auth.models import User
# 导入timezone 处理时间相关的事务
from django.utils import timezone
# 导入 markdown
import markdown
# 导入 strip_tags
from django.utils.html import strip_tags
from taggit.managers import TaggableManager


# 文章分类数据模型
class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    # 函数 __str__ 定义当调用对象的 str() 方法是返回值的内容
    def __str__(self):
        # 返回文章标题
        return self.name
'''
# 文章标签数据模型
class Tag(models.Model):
    name = models.CharField(max_length=100)
    # 函数 __str__ 定义当调用对象的 str() 方法是返回值的内容
    def __str__(self):
        # 返回文章标题
        return self.name
'''

# 博客文章数据模型
class ArticlePost(models.Model):
    # 文章作者
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

    # 文章标题
    title = models.CharField(max_length=100)
    
    # 文章正文
    body = models.TextField()

    # 文章摘要
    excerpt = models.CharField(max_length=200, blank=True)

    # 文章创建时间
    created = models.DateTimeField(default=timezone.now)

    # 文章更新时间
    updated = models.DateTimeField(auto_now=True)

    # 分类、标签与文章关联
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = TaggableManager(blank=True)

    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-created' 表明数据应该以倒序排列
        ordering = ('-created',)

    # 函数 __str__ 定义当调用对象的 str() 方法是返回值的内容
    def __str__(self):
        # 返回文章标题
        return self.title

    def save(self):
        #if not self.excerpt:
            # 实例化Markdown类，用于渲染 body 文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Mark 文本渲染成 HTML
            # 去掉 HTML 标签后取前100个字符给 excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:100]
            super(ArticlePost, self).save()
