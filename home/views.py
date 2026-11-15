from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .models import Product,Categorie,Cart

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

def collectionpage(request):
    products=Product.objects.all()
    return render(request,'collections.html',{'products':products})
    
def cartpage(request,pk):
    products=Cart.objects.filter(user_id=pk)
    return render(request,'cart.html',{'products':products})

def addtocartpage(request,pk):
    product=Product.objects.get(id=pk)
    Cart.objects.create(user=request.user,name=product.name,price=product.price,description=product.description,img=product.img,categorie=product.categorie,size=product.size)
    products=Cart.objects.filter(user_id=request.user.id)
    return render(request,'cart.html',{'products':products})

def deletecart(request, pk):
    if request.method == "POST":
        Cart.objects.filter(id=pk, user=request.user).delete()

    return redirect('/cart/' + str(request.user.id) + '/')