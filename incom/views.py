from django.shortcuts import render,redirect
from .models import CustomUser
from django.contrib.auth.models import  auth
# Create your views here.
def index(request):
    return render(request,'home.html')
def register(request):
    return render(request,'register.html')

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
            else:
                print("Uid Is Not Correct?")

            
            
        else:
            print("error in session creation")
        
        
        return redirect('index')
    except:
        print("error")

def registeraccountbyfacebook(request):
    try:

        name = request.POST.get('name')
        email = request.POST.get('email')
        uid = request.POST.get('uid')
        CustomUser.objects.get_or_create(username=name,first_name=name,email=email,goo_uid=uid)
        user = CustomUser.objects.get(username=name)
        
        if user is not None:
            if uid == user.goo_uid:
                auth.login(request, user)
            else:
                print("Uid Is Not Correct?")

            
            
        else:
            print("error in session creation")
        
        
        return redirect('index')
    except:
        print("error")

def logout(request):
    try:
        auth.logout(request)
        return redirect('index')
    except:
        print("Logout error")

def login(request):
    return render(request,'login.html')