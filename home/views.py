from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .models import Product,Categorie

# Create your views here.

def homepage(request):
    return render(request,'home.html')

def registerpage(request):
    if request.method=="POST":
        first_name=request.POST.get('full_name')
        username=request.POST.get('user_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')

        if User.objects.filter(username=username).exists():
            return render(request,'register.html',{'error':'Username already existed'})
        
        if User.objects.filter(email=email).exists():
            return render(request,'register.html',{'error':'Email already existed'})
        
        if password!=confirm_password:
            return render(request,'register.html',{'error':'Password Mismatching'})
        else:
            user=User.objects.create_user(username=username,first_name=first_name,email=email,password=password)
            return render(request,'register.html',{'success':'User Registration Successfull'})
    else:
        return render(request,'register.html')
    
def loginpage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request,'login.html',{'error':'invalid username or password'})
    else:
        return render(request,'login.html')
    
def logoutpage(request):
    logout(request)
    return redirect('/login/')

def menpage(request):
    products=Product.objects.filter(categorie_id=1)
    return render(request,'men.html',{'products':products})

def womenpage(request):
    products=Product.objects.filter(categorie_id=2)
    return render(request,'women.html',{'products':products})

def accessoriepage(request):
    products=Product.objects.filter(categorie_id=3)
    return render(request,'accessories.html',{'products':products})