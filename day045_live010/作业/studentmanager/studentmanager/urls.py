"""studentmanager URL Configuration

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
    url(r'^class_list/', views.class_list),
    url(r'^class_add/', views.class_add),
    url(r'^class_del/', views.class_del),
    url(r'^class_edit/', views.class_edit),
    url(r'^student_list/', views.student_list),
    url(r'^student_add/', views.student_add),
    url(r'^student_del/', views.student_del),
    url(r'^student_edit/', views.student_edit),
    url(r'^teacher_list/', views.teacher_list),
    url(r'^teacher_add/', views.teacher_add),
    url(r'^teacher_del/', views.teacher_del),
    url(r'^teacher_edit/', views.teacher_edit),
    url(r'', views.index),
]
