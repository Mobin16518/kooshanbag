from django.urls import path
from .views import(
    ZarinpalSendRequest,
    ZarinpalVerify
)

appp_name = "payment"

urlpatterns = [
    path('zarinpal/send/<int:pk>/', ZarinpalSendRequest.as_view(), name='zarinpal_send_request'),
    path('zarinpal/verify/', ZarinpalVerify.as_view(), name="zarinpal_verify")
]