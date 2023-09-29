from django.shortcuts import render
from django.views.generic import View
from products.models import Product
from contact.models import Contact
import random





class Home(View):
    def get(self, request):
        contacts = Contact.objects.all()
        products = Product.objects.all()
        contacts = Contact.objects.all()
        return render(request, 'home/index.html')
