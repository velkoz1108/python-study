"""salary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

# 导入myapp应用视图
from myapp import views as myapp_views, search

urlpatterns = [
    path('', myapp_views.home, name='index'),
    path('add', myapp_views.add),
    path('admin/', admin.site.urls),
    path('new_add2/<int:a>/<int:b>/', myapp_views.addRest, name='add2'),  # name 在页面中 {% url 'add2' 4 5 %} 可以动态解析
    path('add2/<int:a>/<int:b>/', myapp_views.old_add2_redirect),  # 将旧网址转发到新的
    path('list/', myapp_views.list),
    path('search/', search.search),
    path('search-post/', search.search_post),
    path('login', myapp_views.login_view, name='login'),
    path('logout', myapp_views.logout_view),
    path('register', myapp_views.register_view, name='register'),
]
