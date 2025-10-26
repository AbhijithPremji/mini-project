from django.urls import path
from . import views

urlpatterns = [
    path("home/",views.home,name="home"),
    path("cart/",views.cart,name="cart"),
    path("about/",views.about,name="about"),
    path('cart/',views.cart,name="cart"),
    path('grid/',views.grid,name="grid"),
    path('contactuser/',views.Contactuser,name="contactuser"),
    path('singleproduct/<int:pid>/',views.SingleProduct,name="singleproduct"),
    path('user-login/',views.UserLogin,name="userlogin"),
    path('user-register/',views.UserRegist,name="userregist"),
    path('saveuser/',views.SaveUser,name="saveuser"),
    path('LoginUser/',views.LoginUser,name="LoginUser"),
    path('LogoutUser/',views.LogoutUser,name="LogoutUser"),
    path('SaveCart/',views.SaveCart,name="SaveCart"),
    path('SaveWishlist/',views.SaveWishlist,name="SaveWishlist"),
    path('cartdel/<int:pid>/',views.cartdel,name="cartdel"),
    path('PaymentPage/',views.PaymentPage,name="PaymentPage"),
    path('UserAdd/',views.UserAdd,name="UserAdd"),
    path('Checkout/', views.Checkout, name='Checkout'),
    path('wishlist/',views.wishlist,name="wishlist"),
    path('wish/<int:pid>/',views.wish,name="wish")

]