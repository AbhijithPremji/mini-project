from django.urls import path
from . import views


urlpatterns = [
    path('index/',views.home,name="home"),
    path('addcategory/',views.addCategory,name="addCategory"),
    path('categorydetails/',views.CategoryDetails,name="CategoryDetails"),
    path('saveCat/',views.saveCat,name="saveCat"),
    path('catedit/<int:cid>/',views.catedit,name="catedit"),
    path('catupdate/<int:cid>/',views.catupdate,name="catupdate"),
    path('catdel/<int:cid>/',views.catdel,name="catdel"),
    path('addproduct/',views.addProduct,name="addproduct"),
    path('productdetails/',views.ProductDetails,name="productdetails"),
    path('savepro/',views.SaveProduct,name="savepro"),
    path('editpro/<int:pid>/',views.EditPro,name="editpro"),
    path('proupdate/<int:pid>/',views.Proupdate,name="proupdate"),
    path('prodel/<int:pid>/',views.Prodel,name="prodel")

]


