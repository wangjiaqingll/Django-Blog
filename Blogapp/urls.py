from django.urls import path
from . import views

app_name = 'Blogapp'
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'article-detail/<int:id>', views.article_detail, name='article_detail'),
    path(r'article-create/', views.article_create, name='article_create'),
    path(r'article-archives/', views.article_archive, name='article_archives'),
    path(r'article-categories/', views.article_category, name='article_categories'),
    path(r'article-tags/', views.article_tags, name='article_tags'),
    path(r'repository/', views.repository, name='repository'),
    path(r'about/', views.about, name='about'),
    path(r'fleeuestc/', views.fleeuestc, name='fleeuestc')
    
]