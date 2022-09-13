from django.conf.urls import *
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()
from .views import home_page
from .views import authorization
from .views import products
from .views import order,cart

app_name = 'app_website'


urlpatterns = [
    path('', home_page.index, name='index'),
    path(r'^/getSubcategory/$', home_page.get_subcategory),
    path('login', authorization.login, name='login'),
    path('contact_us',home_page.contact_us,name='contact'),
    path('email_check',authorization.emailcheck,name='email_check'),
    path('register',authorization.register,name='register'),
    path('otp_generation',authorization.otp_generation,name='otp_generation'),
    path('otp_verification',authorization.otp_verification,name='otp_verification'),
    path('logout',home_page.logout,name="logout"),
    path('products/<str:pk>/',products.single_page,name="products"),
    path('product_purchase',order.product_purchase,name="product_purchase"),
    path('cart/<str:id>/',cart.cart,name="cart"),
    path('change_quantity_cart',cart.change_quantity,name="change_quantity_cart"),
    path('delete_product',cart.delete_product,name="change_quantity_cart"),
    path('cart_count',cart.cart_count,name="cart_count")
]

