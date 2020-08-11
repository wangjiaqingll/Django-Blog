from django.db import models
# 导入内建的User模型
from django.contrib.auth.models import User
# 导入timezone 处理时间相关的事务
from django.utils import timezone

# 博客文章数据模型
class ArticlePost(models.Model):
    # 文章作者
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

    # 文章标题
    title = models.CharField(max_length=100)
    
    # 文章正文
    body = models.TextField()

    # 文章创建时间
    created = models.DateTimeField(default=timezone.now)

    # 文章更新时间
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-created' 表明数据应该以倒序排列
        ordering = ('-created',)

    # 函数 __str__ 定义当调用对象的 str() 方法是返回值的内容
    def __str__(self):
        # 返回文章标题
        return self.title 
