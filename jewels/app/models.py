from django.db import models


class Register(models.Model):
    Email = models.EmailField(unique=True)
    name = models.TextField()
    phonenumber = models.IntegerField()
    password = models.TextField()
    location= models.TextField()

    def __str__(self):
        return self.name

class Shopreg(models.Model):
    Email = models.EmailField(unique=True)
    name = models.TextField()
    phonenumber = models.IntegerField()
    password = models.TextField()
    location= models.TextField()

    def __str__(self):
        return self.name
    

    
class Product(models.Model):
    shop = models.ForeignKey(Shopreg,on_delete=models.CASCADE)
    name = models.TextField()
    discription = models.TextField()
    price = models.IntegerField()
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
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(Register,on_delete=models.CASCADE)
    date_of_buying = models.TextField()
    payment_status = models.BooleanField(default=False)
    quantity = models.IntegerField()
    price = models.IntegerField()
    del_boy=models.BooleanField(default=False)

    
    def __str__(self):
        return self.product.name
    
class Product_quantity(models.Model):
    productid = models.IntegerField()
    shopid = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.productid
    

class Payment_status(models.Model):
        transactionid = models.IntegerField()
        amount = models.IntegerField()

class delivery(models.Model):
    rout = models.TextField()
    Email =  models.EmailField(unique=True)
    password = models.IntegerField()
    name = models.TextField()
    phonenumber = models.IntegerField()
    def __str__(self):
        return self.name

class delpro(models.Model):
    delivery=models.ForeignKey(delivery,on_delete=models.CASCADE)
    buy=models.ForeignKey(Buy,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    date=models.TextField(null=True) 


class Feedback(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE, related_name='feedbacks')
    message = models.TextField()
    rating = models.IntegerField(default=5)  # 1 to 5 rating
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user.name}"



