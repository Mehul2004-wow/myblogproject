"""
URL configuration for myblogproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views
from blog.views import come_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('wel',views.come_view,name='welcome'),
    path('time',views.current_datetime,name='time'),
    path('blog/<int:id>/', views.blog_int),
    path('blog/<slug:name>/', views.blog_slug),
    path('blog/<str:text>/', views.blog_string),
    path('', views.demo),
    path('About',views.About,name="blog"),
    path('post',views.post,name="post"),
    path('base',views.base),
    path('contact',views.contact, name="contact"),
    path('registration',views.registration, name="registration"),
    path('login',views.login, name="login"),
    path('post',views.post, name="post"),
    path('category',views.category_view, name="category"),
    path('feedback',views.feedback, name="feedback"),
    path('category/edit/<int:id>/', views.edit_category, name='edit_category'),
    path('category/delete/<int:id>/', views.delete_category, name='delete_category'),
]
