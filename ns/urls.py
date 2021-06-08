from . import views
from django.urls import path

urlpatterns=[
    path("",views.home,name="home"),
    path("home/",views.home,name="home"),
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name="logout"),
    path("signup/",views.signup,name="signup"),
    path("changepassword/",views.changepassword,name="changepassword"),
    path("contacts/",views.contacts,name="contacts"),
    path("about/",views.about,name="about"),
    path("services/",views.services,name="services"),
    path("sell/",views.sell,name="sell"),
    path("buy/",views.buy,name="buy"),
    path("sellnew/",views.sellnew,name="sellnew"),
    path("buynew/",views.buynew,name="buynew"),
    path("bid/",views.bid,name="bid"),
    path("cart/",views.cart,name="cart"),
    path("fb/",views.fb,name="fb"),
]