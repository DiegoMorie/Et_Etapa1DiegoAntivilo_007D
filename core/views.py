from django.shortcuts import redirect, render
from .models import USER
from .forms import *
# Create your views here.
#def Temp_all(request):
#    return render(request,'Temp_all.html')


#▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼#

def FirstPage(request):
    return render (request,'FirstPage.html')
def N_template(request):
    return render (request, 'N_Template.html')
def Tecnologia(request):
    return render (request,'Tecnologia.html')
def Deportes (request):
    return render (request,'Deportes.html')
def N_Crea (request):
    return render (request,'N_Crea.html')
#def Usuario (request):
#    return render (request,'core/user.html')


def Ingresar(request):
    if request.method == 'POST' :
        v_desu = formulario_registro(request.POST, files=request.FILES )
        if v_desu.is_valid() :
            v_desu.save()
            return redirect('ver_colaborador')
    else:
        v_desu = formulario_registro()
    return render (request,'core/user.html',{'v_desu':formulario_registro})

def ver_colaborador(request):
    datos= USER.objects.all()
    return render (request,'core/v_colaboradores.html',context={'Datos':datos})

def eliminar(request,id):
    Sus = USER.objects.get(rut=id)
    Sus.delete()
    return redirect ('ver_colaborador')

def Mod (request,id):
    Macaco = USER.objects.get(rut=id)
    datos = {'formulario':formulario_registro(instance=Macaco)}
    if request.method == 'POST' :
        Jex = formulario_registro(data=request.POST,files=request.FILES,instance=Macaco)
        if Jex.is_valid() :
            Jex.save()
            return redirect('ver_colaborador')
    return render (request,'core/mod_col.html',datos)
#▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲#
