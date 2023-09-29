from django.urls import path
from . import views

appp_name = "payment"

urlpatterns = [
    path('zarinpal/send/<int:pk>/', views.ZarinpalSendRequest.as_view(), name = "zarinpal_send_request"),
    path('zarinpal/verify/', views.ZarinpalVerify.as_view(), name="zarinpal_verify")
]