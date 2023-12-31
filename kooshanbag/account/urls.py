from django.urls import path
from . import views



app_name = "account"

urlpatterns = [
    path('user/panel/', views.UserDashbord.as_view(), name='user_dashbord'),
    path('user/login/', views.Userlogin.as_view(), name='user_login'),
    path('user/logout/', views.UserLogout.as_view(), name='user_logout'),
    path('user/register/', views.UserRegister.as_view(), name='user_register'),
    path('user/check/otp/', views.UseerCheckOtp.as_view(), name='user_otp'),
    path('user/add/addres/', views.UserAddAddres.as_view(), name='user_add_addres')
]