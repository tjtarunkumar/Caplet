from django.conf.urls import *
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib import admin

from . import views
from .views import authorization , dashboard

# app_name='admin_panel'

urlpatterns = [
    path('',dashboard.index,name="admin_home_page"),
    path('login',authorization.login ,name="login_page"),
    path('user_login_validation',authorization.user_login_validation ,name="user_login_validation"),
    path('check_credentials',authorization.check_credentials,name="check_credentials")
    ]
