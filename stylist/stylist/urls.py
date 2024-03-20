"""
URL configuration for stylist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from auth import views,AdminViews,StylistViews,ClientViews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('',views.loginPage,name="show_login"),
    path('login',views.Login,name="do_login"),
    path('client_home',ClientViews.client_home,name="client_home"),
    path('stylist_home',StylistViews.stylist_home,name="stylist_home"),
    path('admin_home',AdminViews.admin_home,name="admin_home"),
]
