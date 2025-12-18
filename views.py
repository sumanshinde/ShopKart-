from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm,CustomAuthenticationForm,PasswordResetEmailForm
from django.contrib.auth import authenticate,login,logout
from .models import User
import random

from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import SetPasswordForm
from django.contrib import messages


# Create your views here.

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    else:
        form = CustomUserCreationForm()
        
    context = {
        'form':form
    }
    return render(request,"signup.html",context)


def signin(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request,data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email,password=password)
            if user is not None:
                login(request,user)
                return redirect("index")       
    else:
        form = CustomAuthenticationForm()
        
    context = {
        'form':form
    }

    return render(request,"signin.html",context)

def signout(request):
    logout(request)
    return redirect("signin")



def generate_otp():
    otp = str(random.randint(100000,999999))
    return otp


def forgotPassword(request):
    if request.method == "POST":
        form = PasswordResetEmailForm(data = request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email) 
                otp = generate_otp()
                
                request.session['otp']= otp
                request.session['request_user']= user.id
            
                send_mail(
                        "Password reset OTP",
                        f"Your OTP for password reset is : {otp}",
                        settings.EMAIL_HOST_USER,
                        [user.email],
                        fail_silently=False,
                    )
                return redirect('verify_otp')
                    
            except User.DoesNotExist:
                messages.error(request,"Email does not Exist")
                
  
    else:
        form = PasswordResetEmailForm()   
        
    context= {
        'form':form
    }
    
    return render(request,'forgot-password.html',context)


def verifyOtp(request):
    if request.method=="POST":
        entered_otp = request.POST['otp']
        otp_stored = request.session.get('otp')
        
        if entered_otp == otp_stored:
            user_id = request.session['request_user']
            
            if user_id:
                user = User.objects.get(id=user_id)
                return redirect('reset_password',user_id = user.id) 
            else:
                messages.error(request,"Session Expired")
                
        else:
            messages.error(request,"Invalid OTP")
            
    return render(request,'verify-otp.html')

def resetPassword(request,user_id):
    user = User.objects.get(id=user_id)
    if request.method == "POST":
        form = SetPasswordForm(user=user,data=request.POST)
        if form.is_valid():
            form.save()
            
            if 'otp' in request.session:
                del request.session['otp']
            if 'request_user' in request.session:
                del request.session['request_user']
            
            return redirect("signin")
            
    else:
        form = SetPasswordForm(user=user)
        
        context = {
            'form':form
        }
    return render(request,"reset-password.html",context)