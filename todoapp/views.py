from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from .models import *



def home(request):
    if request.method == 'POST':
        Reja.objects.create(
            sarlavha=request.POST.get("sarlavha"),
            sana=request.POST.get("sana"),
            batafsil=request.POST.get("batafsil"),
            egasi=request.user,
            holati=request.POST.get("holati"),
        )
    if request.user.is_authenticated:
        content={
            "rejalar": Reja.objects.filter(egasi=request.user),
            "foydalanuvchi": request.user.username.capitalize()

        }
        return render(request, 'index.html',content)
    return redirect('/')

def reja_ochir(request,son):
    Reja.objects.get(id=son).delete()
    return redirect('/home/')

def login_view(request):
    if request.method=='POST':
        user=authenticate(
            username= request.POST.get('username'),
            password= request.POST.get('password')
        )
        if user is None:
            return redirect('/')
        login(request,user)
        return redirect('/home/')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')