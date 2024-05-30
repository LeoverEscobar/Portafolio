from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout   
# Create your views here.

def inicio(request):
    return render(request,"pages/inicio.html",{})

@login_required
def portafolio(request):
    return render(request,"pages/portafolio.html",{})

def exit(request):
    logout(request)
    return redirect('inicio')
    