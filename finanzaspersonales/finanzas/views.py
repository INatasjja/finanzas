from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import models
from . import models
from .forms import *



# Create your views here.
def index(request):
    template = 'finanzas/index.html'
    context = {'':''}
    return render(request, template, context)


def transacciones(request):
    template = 'finanzas/transacciones.html'
    context = {'':''}
    return render(request, template, context)

## Usuarios ##
def Usuarios(request):
    contenido = models.usuarios.objects.all()
    template = 'finanzas/usuarios.html'
    context = {'listausuarios': contenido,'':''}
    return render(request, template, context)


def egresos(request):
    contenido = models.TipoEgresos.objects.all()
    template = 'finanzas/tlistado.html'
    context = {'contenido': contenido,'titulo':models.TipoEgresos,'tipot':'e','tipot':'e'}
    return render(request, template, context)

def ingresos(request):
    contenido = models.TipoIngresos.objects.all()
    template = 'finanzas/tlistado.html'
    context = {'contenido': contenido,'titulo':models.TipoIngresos,'tipot':'i'}
    return render(request, template, context)

def tpago(request):
    contenido = models.TipoPago.objects.all()
    template = 'finanzas/tlistado.html'
    context = {'contenido': contenido,'titulo':models.TipoPago,'tipot':'p'}
    return render(request, template, context)

def trenglones(request):
    contenido = models.RenglonEgresos.objects.all()
    template = 'finanzas/tlistado.html'
    context = {'contenido': contenido,'titulo':models.RenglonEgresos,'tipot':'r'}
    return render(request, template, context)

def creausario(request):
    form = UsuarioForm(request.POST)
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.primernombre = form.cleaned_data['primernombre']
            post.segundonombre = form.cleaned_data['segundonombre']
            post.primerapellido = form.cleaned_data['primerapellido']
            post.segundoapellido = form.cleaned_data['segundoapellido']
            post.cedula = form.cleaned_data['cedula']
            post.limiteegresos = form.cleaned_data['limiteegresos']
            post.tipopersona = form.cleaned_data['tipopersona']
            post.fechacorte = form.cleaned_data['fechacorte']
            post.estado = form.cleaned_data['estado']
            post.save()
            return redirect('detalleusuario', pk=post.pk)
        else:
            form = UsuarioForm()

    template = 'finanzas/creausario.html'
    context = {'form': form}
    return render(request, template, context)
 

def editcontenido(request,tipo,id):
    form = EgresoForm(request.POST)
    if request.method == "POST":
        if tipo == 'e':
            form = EgresoForm(request.POST)
            goto = '/tegresos/'
        elif tipo == 'i':
            form = UsuarioForm(request.POST)
            goto = '/tingresos/'
        elif tipo == 'r':
            form = UsuarioForm(request.POST)
            goto = '/trenglones/'        
        elif tipo == 'p':
            form = UsuarioForm(request.POST)
            goto = '/tpagos/'

        if form.is_valid():
            forma = form.save(commit=False)
            forma.descripcion = form.cleaned_data['primernombre']
            forma.estado = form.cleaned_data['segundonombre']
            forma.save()
            return redirect(goto, pk=post.pk)
        else:
            form = UsuarioForm()

    template = 'finanzas/editarcontenido.html'
    context = {'form': form}
    return render(request, template, context)


def elimegreso(request):
    pass