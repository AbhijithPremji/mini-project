from django.shortcuts import render
from Lap.models import CategoryDb,ProductDb

# Create your views here.

def home(req):
    cat = CategoryDb.objects.all()
    products = ProductDb.objects.all()
    pro = products.order_by('?')[:8]
    return render(req,'home.html',{'cat':cat,'pro':pro})

def cart(req):
    return render(req,'cart.html')

def about(req):
    return render(req,'Abouts.html')

def cart(req):
    return render(req,'cart.html')

def grid(req):
    return render(req,'proGrid.html')