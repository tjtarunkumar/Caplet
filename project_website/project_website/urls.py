
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app_website.urls')),
    path('admin_panel/',include('admin_panel.urls'))
]




