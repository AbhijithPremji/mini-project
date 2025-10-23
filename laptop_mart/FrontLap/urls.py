from django.urls import path
from . import views

urlpatterns = [
    path("home/",views.home,name="home"),
    path("cart/",views.cart,name="cart"),
    path("about/",views.about,name="about"),
    path('cart/',views.cart,name="cart"),
    path('grid/',views.grid,name="grid"),
    path('contactuser/',views.Contactuser,name="contactuser"),
    path('singleproduct/<int:pid>/',views.SingleProduct,name="singleproduct")
]