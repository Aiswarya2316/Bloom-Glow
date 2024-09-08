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
    if 'shop' in req.session:
        return redirect(shophome)
    

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
            
            else:
                data=Shopreg.objects.get(Email=email,password=password)
                req.session['shop']=data.Email

                return redirect(shophome)



            messages.warning(req, "INVALID INPUT !")
    return render(req,'login.html')



def logout(req):
    if 'user' in req.session:
        # req.session.flush()
        del req.session['user']
    if 'admin' in req.session:
        del req.session['admin']
    if 'shop' in req.session:
        del req.session['shop']
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
    if req.method=='POST':
        name = req.POST['name']
        discription = req.POST['discription']
        price = req.POST['price']
        category = req.POST['category']
        quantity = req.POST['quantity']
        offerprice = req.POST['offerprice']
        image = req.FILES['image']
        data=Product.objects.create(name=name,discription=discription,price=price,category=category,quantity=quantity,offerprice=offerprice,image=image)
        data.save()
        return redirect(viewpro)
    return render(req,'addpro.html')

    
def viewpro(req):
    data=Product.objects.all()
    return render(req,'viewpro.html',{'data':data})    

def edit(req,id):
    data=Product.objects.get(pk=id)
    if req.method=='POST':
        name1=req.POST['name']
        price=req.POST['price']
        offerprice=req.POST['offerprice']
        quantity=req.POST['quantity']
        image=req.POST['image']
        Product.objects.filter(pk=id).update(name=name1,price=price,offerprice=offerprice,quantity=quantity,image=image)
        return redirect(viewpro)
    return render(req,'edit.html',{'data':data})

def delete(req,id):
    data=Product.objects.get(pk=id)
    data.delete()
    return redirect(viewpro) 