from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('list/', views.ProductList.as_view(), name='products_list'),
    path('list/filter/', views.ProductListFilter.as_view(), name="products_list_filter"),
    path('detail/<int:pk>/<slug:slug>/', views.ProductDetail.as_view(), name='products_detail')
]