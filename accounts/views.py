import random
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import *
from .mixins import MessageHandler


# Create your views here.

def signin(request):
    if request.method == "POST":
        phone_number = request.POST.get("phone_number")
        profile = Profile.objects.get(phone_number = phone_number)
        # if not profile.exists():
        #     return redirect('/signup')
        profile.otp = random.randint(1000,9999)
        profile.save()
        message_handler = MessageHandler(phone_number,profile.otp).send_otp_on_phone()

        return redirect(f'/otp/{profile.uid}')

    return render(request, "signin.html")


def signup(request):
    if request.method == "POST":
        username  = request.POST.get("username") 
        phone_number = request.POST.get("phone_number")
        user  = User.objects.create(username = username)
        profile = Profile.objects.create(user = user , phone_number = phone_number)
        
        return redirect('/')
    return render(request, "signup.html")


def otp(request,uid):
    if request.method == "POST":
        otp = request.POST.get("psw")
        profile = Profile.objects.get(uid=uid)
        if otp == profile.otp:
            login( request,profile.user)
            return redirect('/index')
            
        return redirect(f'/otp/{uid}')


    return render(request, 'otp.html')

def index(request):
    return render(request, "index.html")

