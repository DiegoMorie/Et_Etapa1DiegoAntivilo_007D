from django.db import models

# Create your models here.

class USER (models.Model):
    rut = models.CharField(max_length=10, primary_key=True, verbose_name='Rut', default='0000000')
    name= models.CharField(max_length=30, verbose_name='Nombre Completo')
    cellphone= models.CharField(max_length=30, verbose_name='telefono')
    direction= models.CharField(max_length=30, verbose_name='dirección')
    mail= models.CharField(max_length=30, verbose_name='email')
    city= models.CharField(max_length=30, verbose_name='pais')
    photo= models.ImageField(upload_to='user', blank=True)
    
    def __str__(self):
        return self.rut
