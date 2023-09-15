from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Product, Category


class ProductList(View):
    def get(self, request, category_slug=None):
        category = None
        categories = Category.objects.all()
        products = Product.objects.filter(available=True)
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)
        return render(request,
                  'product/p_list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})
   
   
    
class ProductDetail(View):
    def get(self, request, pk, slug):
        product = get_object_or_404(Product,
                                id=pk,
                                slug=slug,
                                available=True)
        return render(request,'product/p_detail.html',{
            'product' : product
        })
