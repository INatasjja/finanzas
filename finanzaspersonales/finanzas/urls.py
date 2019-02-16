from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tegresos/',views.egresos,name='Tipos de egresos'),
    path('tpagos/',views.tpago,name='Tipos de egresos'),
    path('trenglones/',views.trenglones,name='Tipos de egresos'),
    path('tingresos/',views.ingresos,name='Tipos de egresos'),
    path('edit/<str:tipo>/<int:id>',views.editcontenido,name='Tipos de egresos'),
    path('elimegreso/',views.elimegreso,name='Tipos de egresos'),
    path('creausario',views.creausario,name='Crear usuarios'),
    path('usuarios/',views.Usuarios,name='Usuarios'),
]