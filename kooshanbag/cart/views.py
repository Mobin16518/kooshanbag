from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from products.models import Product
from .cart import Cart
from .forms import CartAddProductForm






class CartDetail(View):
    def get(self, request):
        cart = Cart(request)
        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(initial={
                                            'quantity': item['quantity'],
                                                'override': True})
        return render(request, 'cart/detail.html', {'cart': cart})
    
    


class CartAdd(View):
    def post(self, request, pk):
        cart = Cart(request)
        product = get_object_or_404(Product, id=pk)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product,
                     color=cd['color'],
                     quantity=cd['quantity'],
                     override_quantity=cd['override'])
        return redirect('cart:cart_detail')
    
    
    

class CartRemove(View):
    def post(self, request, pk):
        cart = Cart(request)
        product = get_object_or_404(Product, id=pk)
        cart.remove(product)
        return redirect('cart:cart_detail')