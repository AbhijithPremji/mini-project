from django.db import models

# Create your models here.

class ContactDB(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=50, null=True, blank=True)
    Phone = models.IntegerField(null=True,blank=True)
    Subject = models.CharField(max_length=100,null=True,blank=True)
    Message = models.CharField(max_length=100,null=True,blank=True)

