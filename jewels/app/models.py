from django.db import models

# Create your models here.

class Register(models.Model):
    Email = models.EmailField(unique=True)
    name = models.TextField()
    phonenumber = models.IntegerField()
    password = models.IntegerField()
    location= models.TextField()

    def __str__(self):
        return self.name

class Shopreg(models.Model):
    Email = models.EmailField(unique=True)
    name = models.TextField()
    phonenumber = models.IntegerField()
    password = models.IntegerField()
    location= models.TextField()

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.TextField()
    discription = models.TextField()
    price = models.IntegerField()
    category = models.TextField()
    quantity = models.IntegerField()
    offerprice = models.IntegerField()
    image = models.FileField()

    def __str__(self):
        return self.name
    
class cart(models.Model):
    user = models.ForeignKey(Register,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.user.name +' '+self.product.name
    
    def total_price(self):
        return self.quantity * self.product.price
    
class Buy(models.Model):
    productid = models.IntegerField()
    user = models.TextField()
    date_of_buying = models.IntegerField()
    payment_status = models.IntegerField()
    quantity = models.IntegerField()
    price = models.IntegerField()
    delivery_not = models.TextField()
    
    def __str__(self):
        return self.user
    
class Product_quantity(models.Model):
    productid = models.IntegerField()
    shopid = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.productid
    

class Payment_status(models.Model):
        transactionid = models.IntegerField()
        amount = models.IntegerField()


