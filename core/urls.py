"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from library_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/<int:book_id>', book_detail_view, name='book_detail_url'),
    path('book_create', book_create_view, name='book_create_url'),
    path('book_delete/<int:book_id>', book_delete_view, name='book_delete_url'),
    path('book_update/<int:book_id>', book_update_view, name='book_update_url'),
    path('login', login_view, name='login_url'),
    path('logout', logout_view, name='logout_url'),
    path('', main_view, name='main_url'),
]
