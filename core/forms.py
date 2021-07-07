from django import forms
from django.forms import ModelForm,widgets
from .models import USER

class formulario_registro(ModelForm):
    class Meta:
        model = USER
        fields =['rut','name','photo','mail','cellphone','direction','city',]
        labels={
            'rut': 'rut: ',
            'name': 'Nombre: ',
            'photo': 'Foto',
            'mail': 'mail: ',
            'cellphone': 'Telefono: ',
            'direction': 'Direccion: ',
            'city': 'Pais: ',
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'rut',
                    'placeholder': 'su rut'
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'name',
                    'placeholder': 'su nombre'
                }
            ),
            'photo': forms.FileInput(
                
            ),
            'mail': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'mail',
                    'placeholder': 'su email'
                }
            ),
            'cellphone': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'cellphone',
                    'placeholder': 'su telefono'
                }
            ),
            'direction': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'direction',
                    'placeholder': 'su direccion'
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'city',
                    'placeholder': 'su pais'
                }
            )
        }
