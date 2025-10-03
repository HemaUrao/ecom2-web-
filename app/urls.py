from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.IndexPage, name='index'),
    path('about/', views.AboutPage, name='about'),
    path('products/', views.ProductPage, name='products'),
    path('services/', views.ServicesPage, name='services'),
    path('contact/', views.ContactPage, name='contact'),
    path('base/', views.BasePage, name='base'),
    path('single/', views.SinglePage, name='single'),
    path('cart/',views.CartPage, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    
    
    

]