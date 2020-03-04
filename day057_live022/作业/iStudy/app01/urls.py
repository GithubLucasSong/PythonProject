"""iStudy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    url('^login/$',views.login,name='login'),
    url('^index/$', views.index, name='index'),
    url('^register/$', views.register, name='register'),
    url('^article/(\d+)$', views.article, name='article'),
    url('^personal/(\d+)$', views.personal, name='personal'),
    url('^personal_article/(\d+)$', views.personal_article, name='personal_article'),
    url('^personal_comment/(\d+)$', views.personal_comment, name='personal_comment'),
    url('^article_edit/(\d+)$', views.article_edit, name='article_edit'),
]
