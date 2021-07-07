from django.urls import path
from .views import *

urlpatterns =[
    #path('Temp_all',Temp_all,name='Temp_all'),
    path('',FirstPage,name='FirstPage'),
    path('N_Template',N_template,name='N_Template'),
    path('Tecnologia',Tecnologia,name='Tecnologia'),
    path('Deportes',Deportes,name='Deportes'),
    path('N_Crea',N_Crea,name='N_Crea'),
    path('Ingresar',Ingresar,name='Ingresar'),
    path('Mod/ <id>',Mod,name='Mod'),
    path('eliminar/<id>',eliminar,name='eliminar'),
    path('ver_colaborador',ver_colaborador,name='ver_colaborador'),

]