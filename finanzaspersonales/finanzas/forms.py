from django import forms
from django.forms import ModelForm, Textarea
from .models import usuarios


class UsuarioForm(forms.Form):
    primernombre= forms.CharField(max_length=15,label='Primer Nombre',widget= forms.TextInput(attrs={'class':'form-control','id':'exampleInputName1','placeholder':'Primer Nombre'}))
    segundonombre = forms.CharField(max_length=15,label='Segundo Nombre',widget= forms.TextInput(attrs={'class':'form-control','id':'exampleInputName1','placeholder':'Segundo Nombre'}))
    primerapellido = forms.CharField(max_length=15,label='Primer Apellido',widget= forms.TextInput(attrs={'class':'form-control','id':'exampleInputName1','placeholder':'Primer Apellido'}))
    segundoapellido = forms.CharField(max_length=15,label='Segundo Apellido',widget= forms.TextInput(attrs={'class':'form-control','id':'exampleInputName1','placeholder':'Segundo Apellido'}))
    cedula = forms.CharField(max_length=13,label='Cedula',widget= forms.TextInput(attrs={'class':'form-control','id':'exampleInputName1','placeholder':'Cedula'}))
    limiteegresos = forms.IntegerField(label='Limite de Egresos',widget= forms.TextInput(attrs={'class':'form-control','id':'exampleInputName1','placeholder':'Limite de Egresos'}))
    tipopersona = forms.ChoiceField(label='Tipo Persona',widget= forms.TextInput(attrs={'class':'form-control','id':'exampleInputName1','placeholder':'Tipo Persona'}))
    estado = forms.ChoiceField(label='Estado')


class EgresoForm(forms.Form):
    descripcion = forms.CharField(max_length=15,label='Primer Nombre',widget= forms.TextInput(attrs={'class':'form-control','id':'exampleInputName1','placeholder':'Primer Nombre'}))
    estado = forms.MultipleChoiceField()
