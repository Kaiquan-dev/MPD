"""
URL configuration for myprojectdjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from app1.views import forma
from app1.views import postuser
from app1.views import index_data
from app1.views import my_index
from app1.views import index_users
from app1.views import index_books
from app1.views import index_page
  
urlpatterns = [
    path('admin/', admin.site.urls),
    path("forma/", forma),
    path("forma/postuser/", postuser),
    path('data/', index_data),
    path('', my_index),
    path('users/', index_users),
    path('books/', index_books),
    path('page/', index_page),


]
