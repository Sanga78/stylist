from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,logout
from auth.EmailBackEnd import EmailBackEnd
from django.contrib import  messages
# Create your views here.
def index(request):
    return render(request,'index.html')

def loginPage(request):
    return render(request,'login.html')

def Login(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed !</h2>")
    else:
        user = EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user != None:
            login(request,user)
            if user.user_type == "1":
                return HttpResponseRedirect(reverse("admin_home"))
            elif user.user_type == "2":
                return HttpResponseRedirect(reverse("client_home"))
            else:
                return HttpResponseRedirect(reverse("stylist_home"))
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/")
 