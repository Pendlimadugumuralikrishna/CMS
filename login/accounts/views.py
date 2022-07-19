from unicodedata import name
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import packageform
from .models import package


# Create your views here.
def all_packages(request):
    package_list = package.objects.all()
    return render(request,'packages.html',{'package_list':package_list})
def indexview(request):
    return render(request,"index.html")
@login_required
def dashboardview(request):
     
     package_li = package.objects.all()
     return render(request,"dashboard.html",{'package_list':package_li})

def registerview(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login_url')
    else:
        form = UserCreationForm()

    return render(request,"registration/register.html",{"form":form})
def package_detail(request):
    if request.method == "POST":
        form = packageform(request.POST)
        if form.is_valid():
            form.save()

    form = packageform()
    return render(request,"courier/form.html",{"form":form})
