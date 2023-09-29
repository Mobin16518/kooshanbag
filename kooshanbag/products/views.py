from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView
from django.core.paginator import Paginator
from contact.models import Contact
from .models import Product, Category, Color, Size, Comment, Price
from .forms import CommentForm



contacts = Contact.objects.all()



class ProductList(View):
    def get(self, request):
        products = Product.objects.filter(available=True)
        page_number = request.GET.get('page')
        paginator = Paginator(products, 1)
        products = paginator.get_page(page_number)
        return render(request, 'products/list.html', {
            'products': products, 
            'contacts' : contacts
        })




class ProductListFilter(TemplateView):
    template_name = "products/list_filter.html"
    product = Product.objects.all()
    
    
    def get_context_data(self, **kwargs):
        request = self.request
        category = request.GET.get('category')
        color = request.GET.get('color')
        size = request.GET.get('size')
        price = request.GET.get('price')
        
        categories = Category.objects.all()
        colors = Color.objects.all()
        sizes = Size.objects.all()
        prices = Price.objects.all()
        
        queryset = Product.objects.all()
        
        if category:
            queryset = queryset.filter(category=category).distinct()
            
        if color:
            queryset = queryset.filter(colors=color).distinct()
        
        if size:
            queryset = queryset.filter(size=size).distinct()
        
        if price:
            price = get_object_or_404(Price, id=price)
            queryset = queryset.filter(price__lte=price.max_price, price__gte=price.min_price).distinct()
        
        
        
        page_number = request.GET.get('page')
        paginator = Paginator(queryset, 8)
        queryset = paginator.get_page(page_number)
        
        
        context = super(ProductListFilter, self).get_context_data()
        context = {
            'products' : queryset,
            'category' : category,
            'color' : color,
            'size' : size,
            'price' : price,
            'categories' : categories,
            'colors' : colors,
            'sizes' : sizes,
            'prices' : prices,
            'contacts' : contacts
        }
        return context



    
class ProductDetail(View):
    def get(self, request, pk, slug):
        product = get_object_or_404(Product,
                                id=pk,
                                slug=slug,
                                available=True)
        form = CommentForm
        return render(request,'products/detail.html',{
            'product' : product,
            'contacts' : contacts,
            'form' : form
        })
        
    
    def post(self, request, pk, slug):
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            product = get_object_or_404(Product,
                                         id=pk,
                                         slug=slug,
                                         available=True)
            Comment.objects.create(
                user = request.user, 
                product = product,
                comment = cd['comment']
            )
            return redirect('/')
        return render(request, 'products/detail.html', {'form' : form})
