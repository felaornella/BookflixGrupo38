from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context,loader
from bookflix.models import Usuario
from django.shortcuts import render,redirect
from django.contrib.auth import logout as do_logout, authenticate
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserCreationFormExtends
from django.contrib.auth.models import User
from .models import Perfil,Libro,Autor,Genero,Editorial
import os

# Create your views here.

def iniciarSesion(request):
        return render(request,'inicioSesion.html')

def resultados(request):
    if request.GET["usuario"]:
        buscado=request.GET["usuario"]
        usuario=Usuario.objects.get(email__icontains=buscado)
        return render(request,'resultados.html',{"usuario":usuario})
    else:
        return render(request,'inicioSesion.html')

def register(request):
    form = UserCreationFormExtends()
    if request.method == "POST":
        form = UserCreationFormExtends(data=request.POST)
        if form.is_valid():
            user=form.save()
            prf=Usuario(user=user,dni=form.dni)
            prf.save()

            

            if user is not None:
                do_login(request,user)
                return redirect('/home')
    
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    return render(request, "prueba.html",{'form':form})

def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            do_login(request, user)
            return redirect('/home')
    return render(request, "gestion_usuario/login.html",{'form':form})

def buscarLibro(request):
    return render(request,"busquedaLibro.html")

def resultadosBusqueda(request):
    if request.GET["busqueda"]:
        busq=request.GET["busqueda"]
        resultados=Libro.objects.filter(titulo__icontains=busq)
        #resultados2=Autor.objects.filter(nombre__icontains=busq)
        #resultados3=Editorial.objects.filter(nombre__icontains=busq)
        #resultados4= Genero.objects.filter(nombre__icontains=busq)
        return render(request,"resultadosBusqueda.html",{"resul":resultados,"que":busq},)

def leer(request):
    return render(request,'leer.html')