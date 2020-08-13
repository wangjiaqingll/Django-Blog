from django.urls import path
from . import views

app_name = 'Blogapp'
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'article-detail/<int:id>', views.article_detail, name='article_detail'),
    path(r'article-create/', views.article_create, name='article_create'),
    path(r'article-archives/', views.article_archive, name='article_archives')
]