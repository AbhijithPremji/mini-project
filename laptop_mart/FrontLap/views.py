from django.shortcuts import render,redirect
from Lap.models import CategoryDb,ProductDb
from FrontLap.models import UserRegister,CartDB,UserAddressDB,PaymentDB,WishDB
from django.core.paginator import Paginator
from django.contrib import messages
from django.utils import timezone

# Create your views here.

def home(req):
    cat = CategoryDb.objects.all()
    products = ProductDb.objects.all()
    pro = products = ProductDb.objects.all().order_by('?')[:8]
    prox = ProductDb.objects.all().order_by('?')[:8]
    pross = ProductDb.objects.all().order_by('?')[:8]
    prod = ""
    pros = ""
    for i in prox:
        prod = i
    
    for j in pross:
        pros = j
    return render(req,'home.html',{'cat':cat,'pro':pro,'pros':pros,'prod':prod})

def cart(req):
    return render(req,'cart.html')

def about(req):
    return render(req,'Abouts.html')

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

def UserLogin(req):
    return render(req,'UserLogin.html')

def UserRegist(req):
    return render(req,'UserRegist.html')

def SaveUser(req):
    if req.method == "POST":
        a = req.POST.get("username")
        b = req.POST.get("email")
        c = req.POST.get("password1")
        d = req.POST.get("password2")
        obj = UserRegister(UserName=a, Email=b,Password=c)
        if UserRegister.objects.filter(UserName=a, Password=c).exists():
            messages.error(req, "That user already exists. Please choose another.")
            return redirect(UserLogin)
        obj.save()
        return redirect(UserLogin)  

def LoginUser(req):
    if req.method == "POST":
        us = req.POST.get('email')
        pas = req.POST.get('password')
        a = UserRegister.objects.get(Email=us, Password=pas)
        if UserRegister.objects.filter(Email=us, Password=pas).exists():
            req.session['UserName']= a.UserName
            req.session['Password'] = pas
            req.session['Email'] = us
            return redirect(home)
        else:
            return redirect(UserLogin)

def LogoutUser(req):
    del req.session["UserName"]
    del req.session["Password"]
    del req.session["Email"]
    return redirect(UserLogin)

def SaveCart(req):
    a = req.POST.get('uname')
    b = req.POST.get('price')
    c = req.POST.get('qty')
    d = req.POST.get('total')
    e = req.POST.get('pname')
    obj = CartDB(Price=b, Product=e,Qty=c,Total=d,Username=a)
    obj.save()
    return redirect(home)


def cart(req):
    current_username = req.session.get('UserName')
    data = CartDB.objects.filter(Username=current_username)
    adda = UserAddressDB.objects.filter(Name=current_username)
    names = ""
    add =""
    for i in data:
        names = i

    for i in adda:
        add = i
    tot = 0
    for i in data:
        tot = tot+i.Total

    gst = round(tot*0.05,2) 
    totall = round(tot+gst)
    req.session['grand_total'] = totall
    return render(req,'cart.html',{'data':data,'tot':tot,'gst':gst,'totall':totall,'add':add,'names':names})

def cartdel(req,pid):
    ca = CartDB.objects.filter(id=pid)
    ca.delete()
    return redirect(cart)

def PaymentPage(req):
    current_username = req.session.get('UserName')
    addd = UserAddressDB.objects.filter(Name=current_username)
    data = CartDB.objects.filter(Username=current_username)
    add = ""
    da = ""
    totall = req.session.get('grand_total', 0)
    for i in addd:
        add = i
    
    for i in data:
        da = i
    return render(req,'Payment.html',{'add':add,'da':da,'total':totall})

def UserAdd(req):
    a = req.POST.get('custname')
    b = req.POST.get('code')
    c = req.POST.get('phone')
    d = req.POST.get('address')
    e = req.POST.get('pincode')
    p = b+c
    obj = UserAddressDB(Address=d,Name=a,Phone=p,Pin=e)
    obj.save()
    return redirect(cart)

def SaveWishlist(req):
    a = req.POST.get('uname')
    b = req.POST.get('price')
    c = req.POST.get('qty')
    e = req.POST.get('pname')
    obj = WishDB(Price=b, Product=e,Qty=c,Username=a)
    obj.save()
    return redirect(home)

def wish(req,pid):
    ca = WishDB.objects.filter(id=pid)
    ca.delete()
    return redirect(SaveWishlist)

def wishlist(req):
    current_username = req.session.get('UserName')
    data = WishDB.objects.filter(Username=current_username)
    for i in data:
        names = i
    return render(req,'wishlist.html',{'data':data})


def Checkout(req):
    if req.method == "POST":
        current_username = req.session.get('UserName')
        if not current_username:
            return redirect('UserLogin') 

        # --- THIS IS THE FIX ---
        # Use .first() to get a single address object, or None
        address_obj = UserAddressDB.objects.filter(Name=current_username).first()
        
        if not address_obj:
            # No address found
            messages.error(req, 'Please add a shipping address first.')
            return redirect('cart') 

        pay_method = req.POST.get('payment_method')
        
        cart_items = CartDB.objects.filter(Username=current_username)
        if not cart_items.exists():
            return redirect('home')

        # Your loop logic is correct
        for item in cart_items:
            obj = PaymentDB(
                UserName = current_username,
                Phone = address_obj.Phone,  # This will now work
                Product = item.Product,
                Qty = item.Qty,
                PurchaseDate = timezone.now(), 
                payment_method = pay_method
            )
            obj.save() # This saves the object to PaymentDB
        
        cart_items.delete()
        
        messages.success(req, 'Order Placed Successfully!')
        return redirect('home') 
    
    return redirect('home')
