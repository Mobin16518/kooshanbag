from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from products.models import Product
from contact.models import Contact
from orders.forms import AddresChose
from .cart import Cart
from .forms import CartAddProductForm
from .forms import CouponApplyForm



contacts =Contact.objects.all()



class CartDetail(View):
    def get(self, request):
        cart = Cart(request)
        coupon_apply_form = CouponApplyForm()
        addres_form = AddresChose
        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(initial={
                                            'quantity': item['quantity'],
                                                'override': True})
        return render(request, 'cart/cart.html', {
            'cart': cart,
            'contacts' : contacts,
            'addres_form' : addres_form,
            'coupon_apply_form' : coupon_apply_form, 
        })
    
        


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
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect('cart:cart_detail')