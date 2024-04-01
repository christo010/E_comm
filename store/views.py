from django.shortcuts import render,redirect
from django.views.generic import View,ListView,CreateView
from store.models import Category,Product,cart,order
from store.forms import Register,loginform,orderform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
# Create your views here.

def signinrequired(fn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            return redirect("login")
    return wrapper

class home(ListView):
    model=Category
    template_name="store/index.html"
    context_object_name="categories"
    
class Register(CreateView):
     template_name="store/register.html"
     form_class=Register
     model=User
     success_url=reverse_lazy("home")

class loginview(View):
    def get(self,request,*args,**kwargs):
        form=loginform()
        return render(request,"store/login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=loginform(request.POST)
        if form.is_valid():
            usr=form.cleaned_data.get("username")
            psd=form.cleaned_data.get("password")
            usr_obj=authenticate(request,username=usr,password=psd)
            if usr_obj:
                login(request,usr_obj)
                return redirect("home")
            else:
                form=loginform()
                return render(request,"store/login.html",{"form":form})

     
class Collection(ListView):
    model=Category
    template_name="store/register.html"
    context_object_name="categories"

class Products(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Product.objects.filter(category_id=id)
        name=Category.objects.get(id=id)
        return render(request,"store/category_detail.html",{"data":data,"name":name})
    

class product_detail(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        p_data=Product.objects.filter(id=id)
        return render(request,"store/p_detail.html",{"p_data":p_data})
class signout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")
@method_decorator(signinrequired,name="dispatch")
class Addcart_view(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Product.objects.get(id=id)
        cart.objects.create(items=data,user=request.user)
        return redirect("cartall")
  

class Cartdelete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        cart.objects.get(id=id).delete()
        return redirect("cartall")
@method_decorator(signinrequired,name="dispatch")   
class cartdetailview(View):
    def get(self,request,*args,**kwargs):
        data=cart.objects.filter(user=request.user)
        return render(request,"store/cart.html",{"data":data})
    
class orderview(View):
    def get(self,request,*args,**kwargs):
        form=orderform()
        return render(request,"store/order.html",{"form":form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Product.objects.get(id=id)
        form=orderform(request.POST)
        if form.is_valid():
            qs=form.cleaned_data.get("address")
            order.objects.create(order_item=data,customer=request.user,address=qs)
            return redirect("home")
        return redirect("cartall")

class order_list(View):
    def get(self,request,*args,**kwargs):
        data=order.objects.filter(customer=request.user)
        return render(request,"store/view_order.html",{"data":data})
    
class remove_order(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        order.objects.get(id=id).delete()
        return redirect("cartall")
    
class searchview(View):
    def get(self,request,*args,**kwargs):
        qs=cart.objects.all()

            
    

    
        

        
