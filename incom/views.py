from django.shortcuts import render,redirect
from .models import CustomUser
from django.contrib.auth.models import  auth
from django.http import JsonResponse
from .models import *
# Create your views here.


#The Main Landing Page 
def index(request):
    try:
        if request.user.is_authenticated:
            return redirect('dash')
        else:
            return render(request,'home.html')
    except Exception as e:
         print(e)

#Register Page Rendering
def register(request):
    try:
        return render(request,'register.html')
    except Exception as e:
         print(e)


#Register And Loging With Google Using Ajax
def registerwithgoogle(request):
    try:

        name = request.POST.get('name')
        email = request.POST.get('email')
        uid = request.POST.get('uid')
        CustomUser.objects.get_or_create(username=name,first_name=name,email=email,goo_uid=uid)
        user = CustomUser.objects.get(username=name)
        
        if user is not None:
            if uid == user.goo_uid:
                auth.login(request, user)
                print("Login Succsess")
                return redirect('dash')
            else:
                print("Uid Is Not Correct?")

            
            
        else:
            print("error in session creation")
        
        
        
    except Exception as e:
         print(e)

#Register And Login With Facebook Using Ajax
def registeraccountbyfacebook(request):
    try:

        name = request.POST.get('name')
        email = request.POST.get('email')
        uid = request.POST.get('uid')
        print(name)
        CustomUser.objects.get_or_create(username=name,first_name=name,email=email,goo_uid=uid)
        print(name)
        user = CustomUser.objects.get(username=name)
        
        if user is not None:
            if uid == user.goo_uid:
                auth.login(request, user)
                print("Login Succsess")
                return redirect('dash')
            else:
                print("Uid Is Not Correct?")

            
            
        else:
            print("error in session creation")
        
        
        
    except Exception as e:
         print(e)

#Logout Current User
def logout(request):
    try:
        auth.logout(request)
        return redirect('index')
    except Exception as e:
         print(e)

#Render Login Page
def login(request):
    try:
        return render(request,'login.html')
    except Exception as e:
         print(e)


#Render Dash Page Main User Data Page
def dash(request):
    try:
        return render(request,'maindash.html',{'typename':'DASHBOARD'})
    except Exception as e:
         print(e)

#Income Expence Main Page
def incomeandexpence(request):

    try:
        chart = AmountSet.objects.filter(user=request.user)
        k = 0
        y = 0 
        for cv in chart:
            k = int(k) + cv.debit
            y = int(y) + cv.credit
        return render(request,'dash.html',{'charts':chart,'totinc':k,'totexp':y,'typename':'INCOME & EXPENCE '})
    except Exception as e:
        print(e)
#Create User Accounts 
def addAccoutnt(request):
    try:
        iclist = CharterdOfAccounts.objects.filter(acc_type=1,user=request.user)
        explist = CharterdOfAccounts.objects.filter(acc_type=2,user=request.user)
        paylist = CharterdOfAccounts.objects.filter(acc_type=3,user=request.user)
        return render(request,'add_accounts.html',{'inclists':iclist,'explist':explist,'paylist':paylist})
    except Exception as e:
         print(e)

#create Income Account
def addincomeaccount(request):
    try:
        name = request.POST.get('name')
        
        CharterdOfAccounts.objects.get_or_create(acc_name=name,acc_status=1,acc_type=1,acc_script=10,user=request.user)
        print(name)
        chartu = CharterdOfAccounts.objects.get(acc_name=name,user=request.user)
        AmountSet.objects.create(acc_name=chartu,debit=0,credit=0,user=request.user)
        
        return JsonResponse({'count2': name}, status=200)
        return redirect('dash')
    except Exception as e:
         print(e)

#create Expence Account
def addexpenceaccount(request):
    try:
        name = request.POST.get('name')
        print(name)
        CharterdOfAccounts.objects.create(acc_name=name,acc_status=1,acc_type=2,acc_script=10,user=request.user)
        print(name)
        chartu = CharterdOfAccounts.objects.get(acc_name=name,user=request.user)
        AmountSet.objects.create(acc_name=chartu,debit=0,credit=0,user=request.user)
        return JsonResponse({'count2': name}, status=200)
        return redirect('dash')
    except Exception as e:
         print(e)

#Create Payment Method
def addcustomeraccount(request):
    try:
        name = request.POST.get('accname')
        
        print(name)
        CharterdOfAccounts.objects.create(acc_name=name,acc_status=1,acc_type=3,acc_script=13,user=request.user)
        print(name)
        chartu = CharterdOfAccounts.objects.get(acc_name=name,user=request.user)
        AmountSet.objects.create(acc_name=chartu,debit=0,credit=0,user=request.user)
        return JsonResponse({'count2': name}, status=200)
        return redirect('dash')
    except Exception as e:
         print(e)

#Fetch Datas Of Income Account Name And Expence Account Name And Payment Method Name
def incomeexpence(request):
    try:
        acctypes = CharterdOfAccounts.objects.filter(acc_type=1,acc_script=10,user=request.user)
        acctypese = CharterdOfAccounts.objects.filter(acc_type=2,acc_script=10,user=request.user)
        paytypes = CharterdOfAccounts.objects.filter(acc_type=3,acc_script=13,user=request.user)
        return render(request,'incomeexpence.html',{'acctypes':acctypes,'paytypes':paytypes,'acctypese':acctypese})
    except Exception as e:
         print(e)

#Create Income Transaction
def addincometran(request):
    try:
        amount = request.POST.get('amount')
        acctype = request.POST.get('acctype')
        paytype = request.POST.get('paytype')
        
        chart = CharterdOfAccounts.objects.get(acc_name=acctype,user=request.user)
        print(chart)
        TradeDetails.objects.create(debit_amount=amount,credit_amount=0,acc_name=chart,user=request.user)
        
        JournalEntry.objects.create(acc_name=chart,user=request.user,debit=amount,credit=0,to_acc=paytype,acc_type=1)
        amountchange = AmountSet.objects.get(acc_name=chart,user=request.user)
        print(amountchange)
        print(amountchange.debit)
        totalamount = int(amountchange.debit) + int(amount)
        print(totalamount)
        amountchange.debit = totalamount
        amountchange.save()

        return redirect('dash')
    except Exception as e:
         print(e)

#Create Expence Transaction
def addexpencetran(request):
    try:
        amount = request.POST.get('amount')
        acctype = request.POST.get('acctype')
        paytype = request.POST.get('paytype')
        
        chart = CharterdOfAccounts.objects.get(acc_name=acctype,user=request.user)
        TradeDetails.objects.create(debit_amount=0,credit_amount=amount,acc_name=chart,user=request.user)
        
        JournalEntry.objects.create(acc_name=chart,user=request.user,debit=0,credit=amount,to_acc=paytype,acc_type=1)
        amountchange = AmountSet.objects.get(acc_name=chart,user=request.user)
        print(amountchange.credit)
        totalamount = int(amountchange.credit) + int(amount)
        print(totalamount)
        amountchange.credit = totalamount
        amountchange.save()

        return redirect('dash')
    except Exception as e:
         print(e)

#Details Of Each Transactions

def detailsaofeach(request,acc):
    try:
        chart = CharterdOfAccounts.objects.get(acc_name=acc,user=request.user)
        journal = JournalEntry.objects.filter(acc_name=chart,user=request.user)
        for i in journal:
            print(i)
        return render(request,'detailsoftransaction.html',{'journal':journal,'account':acc})
    except Exception as e:
         print(e)

# Date Wise Income And Expence report
def datewiseincomeexpence(request):
    try:
        journals = JournalEntry.objects.filter(user=request.user)
        return render(request,'datewiseincomeexpence.html',{'journals':journals,'typename':'INCOME & EXPENCE REPORT'})
    except Exception as e:
        print(e)

def datewisefilter(request):
    try:
        date = request.POST.get('name')
        print(date)
        journals = JournalEntry.objects.filter(user=request.user,date_created=date)
        d = {'id':[],'date':[],'account':[],'debit': [], 'credit': [],'toaccount':[]}
        for i in journals:
            print(i.acc_name.acc_name)
            d['id'].append(i.id)
            d['date'].append(i.date_created)
            d['account'].append(i.acc_name.acc_name)
            d['debit'].append(i.debit)
            d['credit'].append(i.credit)
            d['toaccount'].append(i.to_acc)

        print(d)
        return JsonResponse({'count':d},status=200)
        return redirect('dash')
    except Exception as e:
        print(e)