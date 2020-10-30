from django.urls import path
from .views import index,registerwithgoogle,register,registeraccountbyfacebook,logout,login
urlpatterns = [
    path('',index,name="index"),
    path('register',register,name="register"),
    path('registeraccountbygoogle/',registerwithgoogle,name="registeraccountbygoogle"),
    path('registeraccountbyfacebook/',registeraccountbyfacebook,name="registeraccountbyfacebook"),
    path('logout',logout,name="logout"),
    path('login',login,name="login")
   
]
