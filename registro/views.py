from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Persona
from .models import Articulo
from django.contrib.auth import logout


from rest_framework import viewsets
from registro.serializers import PersonaSerializer, ArticuloSerializer
# Create your views here.

#importar user
from django.contrib.auth.models import User, Group
#sistema de autenticación 
from django.contrib.auth import authenticate,logout, login as auth_login

from django.contrib.auth.decorators import login_required



def index(request):
    usuario = request.session.get('usuario',None)
    return render(request,'index.html',{'name':'Registro de personas','personas':Persona.objects.all(),'usuario':usuario})



def donar(request):
    usuario = request.session.get('usuario',None)
    return render(request,'donar.html',{'nameD':'Registro de articulos','articulos':Articulo.objects.all(),'usuario':usuario})

def crearD(request):
    nameD = request.POST.get('nameD','')
    cantidad = request.POST.get('cantidad','')
    desc = request.POST.get('desc','')
    fotoD = request.FILES.get('fotoD',False)
    articulo = Articulo(nameD=nameD,cantidad=cantidad,desc=desc,fotoD = fotoD)
    articulo.save()
    return redirect('donar')

@login_required(login_url='login')
def eliminarD(request,id):
    articulo = Articulo.objects.get(pk = id)
    articulo.delete()
    return redirect('donar')

@login_required(login_url='login')
def cerrar_session2(request):
    del request.session['usuario']
    logout(request)
    return redirect('donar')

def inicio(request):
    return render(request,'inicio.html',{})

def crear(request):
    nombre = request.POST.get('nombre','')
    correo = request.POST.get('correo','')
    contrasenia = request.POST.get('contrasenia','')
    foto = request.FILES.get('foto',False)
    persona = Persona(nombre=nombre,correo=correo,contrasenia=contrasenia,foto = foto)
    persona.save()
    return redirect('index')

@login_required(login_url='login')
def eliminar(request,id):
    persona = Persona.objects.get(pk = id)
    persona.delete()
    return redirect('index')

@login_required(login_url='login')
def editar(request):
    nombre = request.POST.get('nombre','')
    correo = request.POST.get('correo','')
    id = request.POST.get('id',0)
    persona = Persona.objects.get(pk = id)
    persona.nombre = nombre
    persona.correo = correo
    persona.save()
    return redirect('index')

@login_required(login_url='login')
def cerrar_session(request):
    del request.session['usuario']
    logout(request)
    return redirect('index')

def login(request):
    return render(request,'login.html',{})

def login_iniciar(request):
    usuario = request.POST.get('nombre_usuario','')
    contrasenia = request.POST.get('contrasenia','')
    user = authenticate(request,username=usuario, password=contrasenia)

    if user is not None:
        auth_login(request, user)
        request.session['usuario'] = user.first_name+" "+user.last_name
        return redirect("index")
    else:
        return redirect("login")


def hola(request):
    return render(request,'hola.html',{})

def contacto(request):
    return render(request,'contacto.html',{})


def logOut(request):
    logout(request)
    return redirect('/')


class PersonaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Persona.objects.all().order_by('-date_joined')
    serializer_class = PersonaSerializer
 
class ArticuloViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
