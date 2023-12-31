from django.shortcuts import get_object_or_404, redirect
from django.conf import settings
import requests
import json
from django.views.generic import View
from products.models import Product
from orders.models import Order



#? sandbox merchant 
if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'



ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
phone = 'YOUR_PHONE_NUMBER'  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://127.0.0.1:8080/orders/verify/'



class ZarinpalSendRequest(View):
    def get(self, request, pk):
        # instance = get_object_or_404(
        #     Order,
        #     id = pk,
        #     user = request.user
        #     )
        # request.session['order_id'] = str(instance.id)
        # data = {
        # "MerchantID": settings.MERCHANT,
        # "Amount": instance.total_price,
        # "Description": description,
        # "Phone": instance.user.phone,
        # "CallbackURL": CallbackURL,
        # }
        # data = json.dumps(data)
        # # set content length by data
        # headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
        # try:
        #     response = requests.post(ZP_API_REQUEST, data=data, headers=headers, timeout=10)

        #     if response.status_code == 200:
        #         response = response.json()
        #         if response['Status'] == 100:
        #             return {'status': True, 'url': ZP_API_STARTPAY + str(response['Authority']), 'authority': response['Authority']}
        #         else:
        #             return {'status': False, 'code': str(response['Status'])}
        #     return response
    
        # except requests.exceptions.Timeout:
        #     return {'status': False, 'code': 'timeout'}
        # except requests.exceptions.ConnectionError:
        #     return {'status': False, 'code': 'connection error'}
        return redirect('/')




class ZarinpalVerify(View):
    def get(self, request, authority):
        order_id = request.session['order_id']
        order = Order.objects.get(id=int(order_id))
        data = {
        "MerchantID": settings.MERCHANT,
        "Amount": order.total_price,
        "Authority": authority,
        }
        data = json.dumps(data)
        # set content length by data
        headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
        response = requests.post(ZP_API_VERIFY, data=data,headers=headers)

        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                order.paid = True
                order.save()
                return {'status': True, 'RefID': response['RefID']}
            else:
                return {'status': False, 'code': str(response['Status'])}
        return response