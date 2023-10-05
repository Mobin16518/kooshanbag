from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator
from products.models import Product
from contact.models import Contact






class Home(View):
    def get(self, request):
        contacts = Contact.objects.all()
        products = Product.objects.all()
        page_number = request.GET.get('page')
        paginator = Paginator(products, 10)
        products = paginator.get_page(page_number)
        return render(request, 'home/index.html', {
            'products' : products,
            'contacts' : contacts
        })
