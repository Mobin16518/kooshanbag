from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import View
from account.models import UserAddres
from cart.cart import Cart
from .models import OrderItem, Order
from .forms import AddresChose



class OrderCreate(View):
    def post(self, request):
        user = request.user
        cart = Cart(request)
        form = AddresChose(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            instance = get_object_or_404(UserAddres, id=cd['addres'], user=user)
            order = Order.objects.create(
                    f_name = instance.f_name,
                    l_name = instance.l_name,
                    email = instance.email,
                    phone = instance.phone,
                    postal_code = instance.postal_code,
                    city = instance.city,
                    user = instance.user,
                    paid = False,
                )
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            cart.clear()
            # set the order in the session
            request.session['order_id'] = order.id
            # redirect for payment
            return redirect('/')
            