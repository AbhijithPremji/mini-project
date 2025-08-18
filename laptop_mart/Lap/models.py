from django.db import models

# Create your models here.

class CategoryDb(models.Model):
    name = models.CharField(max_length=20,blank=True,null=True)
    image = models.ImageField(upload_to='category/',blank=True,null=True)
    desc = models.CharField(max_length=50,blank=True,null=True)

class ProductDb(models.Model):
    Catname = models.CharField(max_length=20,blank=True,null=True)
    Pname = models.CharField(max_length=20,blank=True,null=True)
    Price = models.IntegerField(blank=True,null=True)
    Desc = models.CharField(max_length=50,blank=True,null=True)
    Pimage1 = models.ImageField(upload_to='product/',blank=True,null=True)
    Pimage2 = models.ImageField(upload_to='product/',blank=True,null=True)


