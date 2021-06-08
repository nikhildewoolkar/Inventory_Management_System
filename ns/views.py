from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.core.exceptions import ObjectDoesNotExist
import datetime
import os
import numpy as np
from .models import UserProfile,SignUp,Feedback,newsell,oldsell
def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def contacts(request):
    return render(request,"contacts.html")
def signup(request):
    # return render(request,"signup.html")
    if request.method=='POST':
        first_name=request.POST.get("fname")
        last_name=request.POST.get("lname")
        username = request.POST.get("uid")
        email=request.POST.get("email")
        password=request.POST.get("pass")
        password1=request.POST.get("pass1")
        address=request.POST.get("add")
        phone=request.POST.get("phoneno")
        gender=request.POST.get("gender")
        def password_check(password):
            SpecialSym =['$', '@', '#', '%'] 
            val = True
            if len(password) < 8:
                print('length should be at least 6') 
                val = False
            if len(password) > 20: 
                print('length should be not be greater than 8') 
                val = False
            if not any(char.isdigit() for char in password): 
                print('Password should have at least one numeral') 
                val = False
            if not any(char.isupper() for char in password): 
                print('Password should have at least one uppercase letter') 
                val = False
            if not any(char.islower() for char in password): 
                print('Password should have at least one lowercase letter') 
                val = False
            if not any(char in SpecialSym for char in password): 
                print('Password should have at least one of the symbols $@#') 
                val = False
            if val == False: 
                val=True
                return val
                print(val)
        if (password_check(password)): 
            print("y")
        else: 
            print("x")
        #print(password)                    
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('signup')
            elif (password_check(password)):
                messages.info(request,'password is not valid')
                print("nick")
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save()
                work=SignUp(username=username,password=password,email=email,first_name=first_name,last_name=last_name,phoneno=phone,address=address)
                work.save()
                messages.info(request,"user created succesfully")
                user=auth.authenticate(username=username,password=password)
                if user is not None:
                   auth.login(request,user)
                print("nikhil")
                u = User.objects.get(username=username)
                reg=UserProfile(user=u,usernames=username,phoneno=phone,address=address)
                reg.save()
                print("dewoolkar")
                auth.logout(request)
                print("nitin")
        else:
            messages.info(request,"password not matching")
            return redirect('signup')
        return redirect('login')
    return render(request,"signup.html")
def login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("pwd")
        print(username)
        print(password)
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return render(request,"home.html")
def changepassword(request):
    # return render(request,"changepassword.html")
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            print("form accepted")
            form.save()
            print(".fds")
            update_session_auth_hash(request, form.user)
            print(".fd")
            messages.success(request, 'Your password was successfully updated!')
            print(".f")
            return redirect('profile')
        else:
            print("erjkevnjfnejnv")
            messages.error(request, 'Please correct the error below.')
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'changepassword.html', args)
def sell(request):
    oldsells=oldsell.objects.all()
    if request.method == 'POST':
        pname=request.POST.get("pname")
        pdesc=request.POST.get("pdesc")
        bid=email=request.POST.get("price")
        pic= request.FILES.get('file')
        date=datetime.datetime.now()
        u=request.user
        print(pic)
        # if(pic!=None):
        reg1=oldsell(name=pdesc,desc=pdesc,bidstart=bid,picture=pic,seller=u.username,date=date)
        reg1.save()
    return render(request,"sell.html",{'oldsells':oldsells})
def buy(request):
    oldsells=oldsell.objects.all()
    return render(request,"buy.html",{'oldsells':oldsells})
def sellnew(request):
    if request.method == 'POST':
        pname=request.POST.get("pname")
        pdesc=request.POST.get("pdesc")
        price=email=request.POST.get("price")
        pic= request.FILES.get("file")
        print(pic)
        quantity=request.POST.get("quantity")
        date=datetime.datetime.now()
        u=request.user
        # if(pic!=None):
        reg2=newsell(name=pdesc,desc=pdesc,price=price,picture=pic,quantity=quantity,seller=u.username,date=date)
        reg2.save()
    return render(request,"sellnew.html")
def buynew(request):
    newsells=newsell.objects.all()
    return render(request,"buynew.html",{'newsells':newsells})
def bid(request):
    return render(request,"bid.html")
def cart(request):
    return render(request,"cart.html")
def services(request):
    return render(request,"services.html")
def fb(request):
    if request.method=="POST":
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        email=request.POST.get("eaddress")
        phone=request.POST.get("tel")
        message=request.POST.get("msg")
        print(fname,lname,phone,email,message)
        register=Feedback(fname=fname,lname=lname ,email=email ,phone=phone ,msg=message)
        register.save()
    return render(request,"contacts.html")