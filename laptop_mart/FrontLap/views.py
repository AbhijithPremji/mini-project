from django.shortcuts import render
from Lap.models import CategoryDb,ProductDb
from django.core.paginator import Paginator

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
    cat = CategoryDb.objects.all()
    prod_list = ProductDb.objects.all()  # Get the full list
    pag = Paginator(prod_list, 6)
    pagnum = req.GET.get('page')
    page_obj = pag.get_page(pagnum)

    return render(req,'proGrid.html',{'cat': cat,'pro': page_obj,'pageobj': page_obj})

def Contactuser(req):
    return render(req,'contactuser.html')

def SingleProduct(req,pid):
    pro = ProductDb.objects.get(id=pid)
    return render(req,'singleProduct.html',{'pro':pro})