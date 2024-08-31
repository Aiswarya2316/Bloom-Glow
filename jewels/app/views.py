from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User,auth
import datetime
# Create your views here.

def get_usr(req):
    data=Register.objects.get(Email=req.session['user'])
    return data


def get_shop(req):
    data=Product.objects.get(category=req.session['shop'])
    return data




def login(req):
    if 'user' in req.session:
        return redirect(userhome)
    if 'admin' in req.session:
        return redirect(adminhome)

    if req.method=='POST':
        email=req.POST['Email']
        password=req.POST['password']
        try:
            data=Register.objects.get(Email=email,password=password)
            req.session['user']=data.Email
            return redirect(userhome)
        except:
            admin=auth.authenticate(username=email,password=password)
            if admin is not None:
                auth.login(req,admin)
                req.session['admin']=email

                return redirect(adminhome)


            messages.warning(req, "INVALID INPUT !")
    return render(req,'login.html')



def logout(req):
    if 'user' in req.session:
        # req.session.flush()
        del req.session['user']
    if 'admin' in req.session:
        del req.session['admin']
    return redirect(login)


def register(req):

    if req.method=='POST':
        name1=req.POST['name']
        email2=req.POST['Email']
        phonenumber3=req.POST['phonenumber']
        location4=req.POST['location']
        password5=req.POST['password']
        try:
            data=Register.objects.create(name=name1,Email=email2,phonenumber=phonenumber3,location=location4,password=password5)
            data.save()
            return redirect(login)
        except:
            messages.warning(req, "Email Already Exits , Try Another Email.")
    return render(req,'register.html')


def shopregister(req):

    if req.method=='POST':
        name1=req.POST['name']
        email2=req.POST['Email']
        phonenumber3=req.POST['phonenumber']
        location4=req.POST['location']
        password5=req.POST['password']
        try:
            data=Shopreg.objects.create(name=name1,email=email2,phonenumber=phonenumber3,location=location4,password=password5)
            data.save()
            return redirect(login)
        except:
            messages.warning(req, "Email Already Exits , Try Another Email.")
    return render(req,'shopregister.html')
    print(shopregister)


def userhome(req):
    if 'user' in req.session:
        return render(req,'userhome.html')
    else:
        return redirect(login)

def adminhome(req):
    
    return render(req,'adminhome.html')


def shophome(req):
    
    return render(req,'shophome.html')

def addpro(req):
    
    return render(req,'addpro.html')

def viewpro(req):

    return render(req,'viewpro.html')    