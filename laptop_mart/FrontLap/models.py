from django.db import models
from django.utils import timezone

# Create your models here.

class ContactDB(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=50, null=True, blank=True)
    Phone = models.IntegerField(null=True,blank=True)
    Subject = models.CharField(max_length=100,null=True,blank=True)
    Message = models.CharField(max_length=100,null=True,blank=True)

class UserRegister(models.Model):
    UserName = models.CharField(max_length=50,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Password = models.CharField(max_length=100,null=True,blank=True)

class CartDB(models.Model):
    Username = models.CharField(max_length=50,null=True,blank=True)
    Product = models.CharField(max_length=50,null=True,blank=True)
    Qty = models.IntegerField(null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Total = models.IntegerField(null=True,blank=True)

class WishDB(models.Model):
    Username = models.CharField(max_length=50,null=True,blank=True)
    Product = models.CharField(max_length=50,null=True,blank=True)
    Qty = models.IntegerField(null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)


class UserAddressDB(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Phone =  models.IntegerField(null=True,blank=True)
    Address = models.CharField(max_length=100,null=True,blank=True)
    Pin =  models.IntegerField(null=True,blank=True)

class PaymentDB(models.Model):
    UserName = models.CharField(max_length=50,null=True,blank=True)
    Phone = models.IntegerField(null=True,blank=True)
    Product = models.CharField(max_length=50,null=True,blank=True)
    Qty = models.IntegerField(default=1)
    PurchaseDate = models.DateTimeField(default=timezone.now)
    PayMethod = [
        ('COD', 'Cash on Delivery'),
        ('CARD', 'Credit/Debit Card'),
        ('UPI', 'UPI'),
    ]
    payment_method = models.CharField(max_length=10, choices=PayMethod, default='COD')


