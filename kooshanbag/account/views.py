from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from django.urls import reverse
from kooshanbag.settings import GAHSEDAK_API_KEY
from django.views.generic import View
from .models import User, Otp
from .forms import (
    LoginForm,
    RegisterForm,
    CheckOtpForm
)
from random import randint


SMS = GAHSEDAK_API_KEY



class Userlogin(View):
    def get(self , request):
        if request.user.is_authenticated == True:
             return redirect('/')
        else:
            form = LoginForm
            return render(request, 'account/login.html', {'form':form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect("/")
        return render(request, 'account/login.html', {'form':form})



class UserRegister(View):
     def get(self, request):
        if request.user.is_authenticated == True:
            return redirect('/')
        else:
            # contact = Contact.objects.all()
            form = RegisterForm()
            return render(request, 'account/register.html', {'form':form})
     

     def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['password'] == cd['password_conf']:
                if cd['password_conf'] <= 16 and cd['password_conf'] >= 8 :
                    random_code = randint(100000, 999999)
                    SMS.verification({
                        'reseptor' : cd['phone'],
                        'template' : 'template_name',
                        'type' : '1',
                        'param1' : random_code
                    })
                    token = get_random_string(length=100)
                    Otp.objects.create(email=cd['email'], phone=cd['phone'], password=cd['password'],
                                       f_name=cd['fname'], l_name=cd['lname'], otp_code=[random_code], token=token)
                                
                    return redirect(reverse('account:user_otp' + f'?token={token}'))
                else:
                    form.add_error('password_conf', 'رمز عبور وارد شده کوچکتر از ۸ و یا بزرگتر از ۱۶ است')
            else:
                form.add_error('password_conf', 'رمز عبور خود را اشتباه وارد کردید')

        return render(request, 'account/register.html', {'form':form})
     

class UseerCheckOtp(View):
    def get(self, request):
        if request.user.is_authenticated == True:
            return redirect('/')
        else:
            form = CheckOtpForm
            return render(request, 'account/chekotp.html', {'form':form})
    
    def post(self, request):
        token = request.GET.get('token')
        form = CheckOtpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            otp = Otp.objects.filter(otp_code=cd['code'], token=token)
            if otp.exists():
                user = User.objects.create_user(email=cd['email'], phone=cd['phone'],
                                                fname=otp.f_name, lname=otp.l_name)
                login(request, user)
                return redirect('/')
            else:
                form.add_error('code', 'معتبر نیست')
                



class UserLogout(View):
    def get(self, request):
        logout(request)
        return redirect('/')



class UserDashbord(View):
    def get(self, request):
        # Check if the user dashboard is the same user that sent the request
        if request.user.is_authenticated == True:
            user = request.user
            # Render the dashboard template
            return render(request, 'dashboard.html', {
                'user' : user
            })
        else:
            # Redirect to the login page if the user dashboard is not the same user
            return redirect('account/user_login')
