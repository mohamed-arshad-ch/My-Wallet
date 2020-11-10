from django.urls import path
from .views import index,registerwithgoogle,register,registeraccountbyfacebook,logout,login,dash,addAccoutnt,addincomeaccount,addexpenceaccount,addcustomeraccount,incomeexpence,addincometran,addexpencetran,detailsaofeach,incomeandexpence,datewiseincomeexpence,datewisefilter,lendingpage,addlendingpage,addcustomeraccountinlending,addlendingtransactio,addyougottransaction,addyougivetransaction

urlpatterns = [
    path('',index,name="index"),
    path('register',register,name="register"),
    path('registeraccountbygoogle/',registerwithgoogle,name="registeraccountbygoogle"),
    path('registeraccountbyfacebook/',registeraccountbyfacebook,name="registeraccountbyfacebook"),
    path('logout',logout,name="logout"),
    path('login',login,name="login"),
    path('dash',dash,name="dash"),
    path('incomeandexpence',incomeandexpence,name="incomeandexpence"),
    path('addaccount',addAccoutnt,name="addaccount"),
    path('addincacc/',addincomeaccount,name="addincacc"),
    path('addexpenceaccount/',addexpenceaccount,name="addexpenceaccount"),
    path('addcustomeraccount/',addcustomeraccount,name="addcustomeraccount"),
    path('incomeexpence',incomeexpence,name="incomeexpence"),
    path('addincometran/',addincometran,name="addincometran"),
    path('addexpencetran/',addexpencetran,name="addexpencetran"),
    path('detailsaofeach/<str:acc>',detailsaofeach,name="detailsaofeach"),
    path('datewiseincomeexpence',datewiseincomeexpence,name="datewiseincomeexpence"),
    path('datewisefilter/',datewisefilter,name="datewisefilter"),
    path('lendingmoney',lendingpage,name="lendingpage"),
    path('addlendingpage',addlendingpage,name="addlendingpage"),
    path('addcustomeraccountinlending/',addcustomeraccountinlending,name="addcustomeraccountinlending/"),
    path('addlendingtransactio',addlendingtransactio,name="addlendingtransactio"),
    path('addyougottransaction/',addyougottransaction,name="addyougottransaction"),
    path('addyougivetransaction/',addyougivetransaction,name="addyougivetransaction")

   
]
