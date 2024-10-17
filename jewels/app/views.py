from django.shortcuts import render,redirect
from .models import *
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
import re
from django.contrib.auth.models import User,auth
import datetime
# Create your views here.

def get_usr(req):
    data=Register.objects.get(Email=req.session['user'])
    return data


def get_shop(req):
    data=Shopreg.objects.get(Email=req.session['shop'])
    return data

def get_product(req):
    data=Product.objects.get(shop=req.session['product'])
    return data


def login(req):
    if 'user' in req.session:
        return redirect(userhome)
    if 'admin' in req.session:
        return redirect(adminhome)
    if 'shop' in req.session:
        return redirect(shophome)
    

    if req.method=='POST':
        Email=req.POST['Email']
        password=req.POST['password']
        try:
            data=Register.objects.get(Email=Email,password=password)
            req.session['user']=data.Email
            return redirect(userhome)
        except Register.DoesNotExist:
            admin=auth.authenticate(username=Email,password=password)
            if admin is not None:
                auth.login(req,admin)
                req.session['admin']=Email

                return redirect(adminhome)
            
            else:
                try:
                    data=Shopreg.objects.get(Email=Email,password=password)
                    req.session['shop']=data.Email

                    return redirect(shophome)
                except Shopreg.DoesNotExist:


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
         # Validate email
        try:
            validate_email(email2)
        except ValidationError:
            messages.warning(req, "Invalid email format, please enter a valid email.")
            return render(req, 'register.html')

        # Validate phone number (assuming 10-digit numeric format)
        if not re.match(r'^\d{10}$', phonenumber3):
            messages.warning(req, "Invalid phone number. Please enter a valid 10-digit phone number.")
            return render(req, 'register.html')
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
            data=Shopreg.objects.create(name=name1,Email=email2,phonenumber=phonenumber3,location=location4,password=password5)
            data.save()
            return redirect(login)
        except:
            messages.warning(req, "Email Already Exits , Try Another Email.")
    return render(req,'shopregister.html')
    print(shopregister)


def userhome(req):
    if 'user' in req.session:
        data=Product.objects.all()
        return render(req,'userhome.html',{'data':data})
    else:
        return redirect(login)

def adminhome(req):
    
    return render(req,'adminhome.html')


def shophome(req):
    
    return render(req,'shophome.html')

def deliverys(req):
    
    return render(req,'deliveryhome.html')

def addpro(req):
    if req.method=='POST':
        name = req.POST['name']
        discription = req.POST['discription']
        price = req.POST['price']
        quantity = req.POST['quantity']
        offerprice = req.POST['offerprice']
        image = req.FILES['image']
        data=Product.objects.create(name=name,discription=discription,price=price,quantity=quantity,offerprice=offerprice,image=image,shop=get_shop(req))
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
        image=req.FILES.get('image')
        print(type(image))
        if image:

         Product.objects.filter(pk=id).update(name=name1,price=price,offerprice=offerprice,quantity=quantity)
         data=Product.objects.get(pk=id)
         data.image=image
         data.save()
        else:
            Product.objects.filter(pk=id).update(name=name1,price=price,offerprice=offerprice,quantity=quantity)
        return redirect(viewpro)
    return render(req,'edit.html',{'data':data})

def delete(req,id):
    data=Product.objects.get(pk=id)
    data.delete()
    return redirect(viewpro) 


###profile of user
def profile(req):
    if 'user' in req.session:
        # data=Register.objects.get(Email=req.session['user'])
        return render(req,'userprofile.html',{'data':get_usr(req)})
    else:
        return redirect(login)
    

###profile update
def upload(req):
    if 'user' in req.session:
        data=Register.objects.get(Email=req.session['user'])
        if req.method=='POST':
            name=req.POST['name']
            phonenumber=req.POST['phonenumber']
            location=req.POST['location']
            Register.objects.filter(Email=req.session['user']).update(name=name,phonenumber=phonenumber,location=location)
            return redirect(profile)
        return render(req,'updateprofile.html',{'data':data})

    else:
       return redirect(login)
    
def userviewproduct(req):
    data=Product.objects.all()
    return render(req,'userviewproduct.html',{'data':data})

def prodetails(req,id):
    data=Product.objects.get(pk=id)
    return render(req,'prodetails.html',{'data':data})

def shopprodetails(req,id):
    data=Product.objects.get(pk=id)
    return render(req,'shopprodetails.html',{'data':data})



def user_cart(req,id):
    if 'user' in req.session:
        product=Product.objects.get(pk=id)
        user=get_usr(req)
        qty=1
        try:
            dtls=cart.objects.get(product=product,user=user)
            dtls.quantity+=1
            dtls.save()
        except:
            data=cart.objects.create(product=product,user=user,quantity=qty)
            data.save()
        return redirect(user_view_cart)
    else:
        return redirect(login)
    
def user_view_cart(req):
    if 'user' in req.session:
        data=cart.objects.filter(user=get_usr(req))
        return render(req,'addtocart.html',{'data':data})
def qty_incri(req,id):
    data=cart.objects.get(pk=id)
    data.quantity+=1
    data.save()
    return redirect(user_view_cart)

def qty_decri(req,id):
    data=cart.objects.get(pk=id)
    if data.quantity>1:
        data.quantity-=1
        data.save()
    return redirect(user_view_cart)

def buynow(req,id):
     if 'user' in req.session:
        cart_product=cart.objects.get(pk=id)
        user=get_usr(req)
        quantity=cart_product.quantity
        date=datetime.datetime.now().strftime("%x")
        price=cart_product.product.price
        order=Buy.objects.create(product=cart_product.product,user=user,quantity=quantity,date_of_buying=date,price=price)
        order.save()
        return redirect(user_view_cart)
     
def deleteitem(req,id):
    data=cart.objects.get(pk=id)
    data.delete()
    return redirect(user_view_cart)

def orderdetails(req):
    data=Buy.objects.filter(user=get_usr(req))
    return render(req,'orderdetails.html',{'data':data})
    
def delregister(req):

    if req.method=='POST':
        name1=req.POST['name']
        email2=req.POST['Email']
        phonenumber3=req.POST['phonenumber']
        location4=req.POST['rout']
        password5=req.POST['password']
    
        try:
            data=delivery.objects.create(name=name1,Email=email2,phonenumber=phonenumber3,rout=location4,password=password5)
            data.save()
            return redirect(login)
        except:
            messages.warning(req, "Email Already Exits , Try Another Email.")
    return render(req,'deliveryreg.html')
    print(delregister)




def viewshop(req):
    data=Shopreg.objects.all()
    return render(req,'viewshop.html',{'data':data})

def aboutus(req):
    
    return render(req,'aboutus.html')

def contact(req):
    
    return render(req,'contact.html')

def service(req):
    
    return render(req,'service.html')

def bookinghistry(req):
    #  if 'shop' in req.session:
    l=[]
    data=Product.objects.filter(shop=get_shop(req))
    for i in data:
        data1=Buy.objects.filter(product=i)
        l.append(data1)
    print(l)
    # data1=delivery.objects.all()
    return render(req,'bookinghistry.html',{'data':l})


def search_by_category(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category')
    products = Product.objects.filter(category__name=selected_category) if selected_category else Product.objects.all()

    return render(request, 'search.html', {
        'products': products,
        'categories': categories,
        'selected_category': selected_category
    })
