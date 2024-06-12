from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('storeHome/', views.storeHome, name='storeHome'),
    path('vendorHome/', views.vendorHome, name='vendorHome'),
    path('stores/', views.store_list, name='store_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('buy_now/<int:product_id>/', views.buy_now, name='buy_now'),
    path('manage_store/', views.manage_store, name='manage_store'),
    path('vendor/products/', views.vendor_products, name='vendor_products'),
    path('vendor/products/create/', views.create_product, name='create_product'),
    path('vendor/profile/', views.vendor_profile, name='vendor_profile'),
    
]

# http://127.0.0.1:8000/tienda/product/1/