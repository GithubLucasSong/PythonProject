"""bookmanager URL Configuration

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
    url(r'^admin/', admin.site.urls),
    url(r'index', views.Index.as_view()),
    url(r'^pl/', views.publisher_list,name='publisher_list'),
    url(r'^pa/', views.Publisher_add.as_view(),name='publisher_add'),
    url(r'^pd/(\d+)', views.publisher_del,name='publisher_del'),
    url(r'^pe/(\d+)', views.publisher_edit,name='publisher_edit'),
    url(r'^book_list/', views.book_list),
    url(r'^book_add/', views.book_add),
    url(r'^book_del/', views.book_del),
    url(r'^book_edit/', views.book_edit),
    url(r'^author_list/', views.author_list),
    url(r'^author_add/', views.author_add),
    url(r'^author_del/', views.author_del),
    url(r'^author_edit/', views.author_edit),
    url(r'^dele/(\w+)/(\d+)', views.dele),

]
