from django.conf.urls import include
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from accounts import views

urlpatterns = [
    path('accounts/login/', views.login, name='login'),
]