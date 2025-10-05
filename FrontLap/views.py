from django.shortcuts import render

# Create your views here.

def home(req):
    return render(req,'home.html')

def cart(req):
    return render(req,'cart.html')

def about(req):
    return render(req,'Abouts.html')

def cart(req):
    return render(req,'cart.html')

def grid(req):
    return render(req,'proGrid.html')