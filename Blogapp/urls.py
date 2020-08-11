from django.urls import path
from . import views

app_name = 'Blogapp'
urlpatterns = [
    path(r'index/', views.index, name='index')
]