from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('/list', views.ProductList.as_view(), name='product_list'),
    path('list/<slug:category_slug>/', views.ProductList.as_view(), name='product_list_by_category'),
    path('product/detail/<int:pk>/<slug:slug>/', views.ProductDetail.as_view(), name='product_detail')
]