from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, TemplateView
from django.core.paginator import Paginator
from contact.models import Contact
from .models import Product, Category, Color, Size



class ProductList(View):
    def get(self, request):
        contacts = Contact.objects.all()
        products = Product.objects.filter(available=True)
        page_number = request.GET.get('page')
        paginator = Paginator(products, 15)
        products = paginator.get_page(page_number)
        return render(request, 'products/list.html', {
            'products': products, 
            'contacts' : contacts
        })




class ProductListFilter(TemplateView):
    template_name = "products/list_filter.html"
    product = Product.objects.all()
    categories = Category.objects.all()
    color = Color.objects.all()
    size = Size.objects.all()
    
    
    def get_context_data(self, **kwargs):
        request = self.request
        category = request.GET.getlist('category')
        colors = request.GET.getlist('color')
        size = request.GET.getlist('size')
        
        queryset = Product.objects.all()
        
        if category:
            queryset = queryset.filter(category__title__in=category)
            
        if colors:
            queryset = queryset.filter(color=colors)
        
        if size:
            queryset = queryset.filter(size=size)
        
        page_number = request.GET.get('page')
        paginator = Paginator(queryset, 15)
        queryset = paginator.get_page(page_number)
        
        
        context = super(ProductListFilter, self).get_context_data()
        context = {
            'products' : queryset,
            'category' : category,
            'color' : colors,
            'size' : size
        }
        return context




    
class ProductDetail(View):
    def get(self, request, pk, slug):
        contacts = Contact.objects.all()
        product = get_object_or_404(Product,
                                id=pk,
                                slug=slug,
                                available=True)
        return render(request,'products/detail.html',{
            'product' : product,
            'contacts' : contacts
        })
