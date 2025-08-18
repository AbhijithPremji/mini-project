from django.shortcuts import render,redirect
from Lap.models import CategoryDb,ProductDb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.

def home(req):
    return render(req,'index.html')

def addCategory(req):
    return render(req,'addCategory.html')

def CategoryDetails(req):
    pro = CategoryDb.objects.all()
    return render(req,'CategoryDetails.html',{'pro':pro})

def saveCat(req):
    if req.method == "POST":
        a = req.POST.get('sname')
        b = req.POST.get('desc')
        img = req.FILES['file']
        obj = CategoryDb(name=a,image=img,desc=b)
        obj.save()
        return redirect(CategoryDetails)

def catedit(req,cid):
    data = CategoryDb.objects.get(id=cid)
    return render(req,'editCategory.html',{'data':data})

def catupdate(req,cid):
     if req.method == "POST":
        a = req.POST.get('sname')
        b = req.POST.get('desc')
        try:
            img = req.FILES['file']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = CategoryDb.objects.get(id=cid).img
        CategoryDb.objects.filter(id=cid).update(name=a,image=file,desc=b)
        return redirect(CategoryDetails)

def catdel(req,cid):
    data = CategoryDb.objects.filter(id=cid)
    data.delete()
    return redirect(CategoryDetails)

        
def addProduct(req):
    prod = CategoryDb.objects.all
    return render(req,'addProduct.html',{'prod':prod})

def ProductDetails(req):
    pro = ProductDb.objects.all()
    return render(req,'ProductDetails.html',{'pro':pro})

def SaveProduct(req):
    if req.method == "POST":
        pname = req.POST.get('pname')
        cname = req.POST.get('cname')
        p = req.POST.get('price')
        des = req.POST.get('desc')
        img1 = req.FILES['pimg1']
        img2 = req.FILES['pimg2']
        obj = ProductDb(Catname=cname,Pname=pname,Price=p,Desc=des,Pimage1=img1,Pimage2=img2)
        obj.save()
    return redirect(ProductDetails)

def EditPro(req,pid):
    cat = CategoryDb.objects.all()
    pro = ProductDb.objects.get(id=pid)
    return render(req,'editProduct.html',{'cat':cat,'pro':pro})

def Proupdate(req,pid):
     if req.method == "POST":
        a = req.POST.get('cname')
        e = req.POST.get('pname')
        b = req.POST.get('price')
        c = req.POST.get('desc')
        try:
            img1 = req.FILES['pimg1']
            fs = FileSystemStorage()
            file1 = fs.save(img1.name,img1)
        except MultiValueDictKeyError:
            file1 = ProductDb.objects.get(id=cid).Pimage1
        try:
            img2 = req.FILES['pimg2']
            fs = FileSystemStorage()
            file2 = fs.save(img2.name,img2)
        except MultiValueDictKeyError:
            file2 = ProductDb.objects.get(id=cid).Pimage1

        ProductDb.objects.filter(id=pid).update(Catname=a,Pname=e,Price=b,Desc=b,Pimage1=file1,Pimage2=file2)
        return redirect(ProductDetails)

def Prodel(req,pid):
    pro = ProductDb.objects.filter(id=pid)
    pro.delete()
    return redirect(ProductDetails)
