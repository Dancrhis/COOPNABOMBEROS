
from datetime import datetime
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class Socio(models.Model):
    
    fechaSolicitud=models.DateTimeField(default=datetime.now())
    usuario=models.ForeignKey(User, on_delete=models.CASCADE)
    estado=models.CharField(max_length=50, default="solicitud")
    fechaValidacion=models.DateTimeField(null=True)
    acta=models.CharField(max_length=100, null=True)
    

    cedula=models.IntegerField(primary_key=True)
    nombre1=models.CharField(max_length=100, null=False)
    nombre2=models.CharField(max_length=100, null=True)
    apellido1=models.CharField(max_length=100, null=False)
    apellido2=models.CharField(max_length=100, null=True)
    fechaNacimiento=models.DateField()
    nacionalidad=models.CharField(max_length=100)
    sexo=models.CharField(max_length=1)
    provincia=models.CharField(max_length=100)
    municipio=models.CharField(max_length=100)
    sector=models.CharField(max_length=100)
    estadoCivil=models.CharField(max_length=100)
    telefono=models.IntegerField()
    celular=models.IntegerField()
    lugarTrabajo=models.CharField(max_length=100)
    cargo=models.CharField(max_length=100)
    telefonoLugarTrabajo=models.IntegerField()

class Beneficiario(models.Model):
    afiliado=models.ForeignKey(Socio, on_delete=models.CASCADE)
    cedula=models.IntegerField(null=False)
    nombre1=models.CharField(max_length=100, null=False)
    nombre2=models.CharField(max_length=100, null=True)
    apellido1=models.CharField(max_length=100, null=False)
    apellido2=models.CharField(max_length=100, null=True)
    parentezco=models.CharField(max_length=50)
    porcentaje=models.IntegerField()


class Slider(models.Model):
    image= models.ImageField(upload_to='static/IMG/images/%y/%m/%d')
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

