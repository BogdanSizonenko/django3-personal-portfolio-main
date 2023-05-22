from django.urls import path
from . import views #Точка для импорта views, потому что этот файл в той же папке что views.py

app_name = 'blog'

urlpatterns = [
    path ('', views.all_blogs, name='all_blogs'),
    path ('<int:blog_id>/', views.detail, name='detail'),
]