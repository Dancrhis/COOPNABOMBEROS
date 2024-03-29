
from datetime import datetime
from distutils.command.upload import upload
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



# Create your models here.


class Socio(models.Model):
    ESTADOS=[("en proceso","en proceso"),
            ("aprobada","aprobada"),
            ("rechazada","rechazada"),]
    fechaSolicitud=models.DateTimeField( auto_now_add=True)
    usuario=models.OneToOneField(User,to_field='username', on_delete=models.CASCADE)
    estado=models.CharField(max_length=50, default="en proceso", choices=ESTADOS, editable=True)
    fechaValidacion=models.DateTimeField(null=True,default=timezone.now)
    acta=models.CharField(max_length=100, null=True, default="ninguna")
    

    cedula=models.BigIntegerField(primary_key=True)
    nombre1=models.CharField(max_length=100, null=False)
    nombre2=models.CharField(max_length=100, null=True, blank=True)
    apellido1=models.CharField(max_length=100, null=False)
    apellido2=models.CharField(max_length=100, null=True, blank=True)
    fechaNacimiento=models.DateField()
    nacionalidad=models.CharField(max_length=100)
    sexo=models.CharField(max_length=1)
    provincia=models.CharField(max_length=100)
    municipio=models.CharField(max_length=100)
    sector=models.CharField(max_length=100)
    estadoCivil=models.CharField(max_length=100)
    telefono=models.BigIntegerField(null=True, blank=True)
    celular=models.BigIntegerField(null=True, blank=True)
    lugarTrabajo=models.CharField(max_length=100)
    cargo=models.CharField(max_length=100)
    telefonoLugarTrabajo=models.BigIntegerField()
    institucionAtencionEmergencia=models.CharField(max_length=400, null=True)
    ubicacion=models.CharField(max_length=400, null=True)
    banco=models.CharField(max_length=400, null=True)
    numeroCuenta=models.BigIntegerField(null=True)
    aporte=models.IntegerField(default=0)

class Beneficiario(models.Model):
    afiliado=models.ForeignKey(User,to_field='username', on_delete=models.CASCADE)
    cedula=models.BigIntegerField(null=False)
    nombre1=models.CharField(max_length=100, null=False)
    nombre2=models.CharField(max_length=100, null=True,blank=True)
    apellido1=models.CharField(max_length=100, null=False)
    apellido2=models.CharField(max_length=100, null=True,blank=True)
    parentezco=models.CharField(max_length=50)
    porcentaje=models.IntegerField()
    telefono=models.BigIntegerField()


class Slider(models.Model):
    image= models.ImageField( upload_to="images/%y%m%d",null=True,blank=True)
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Noticia(models.Model):
    foto=models.ImageField( upload_to="images/%y%m%d",null=True,blank=True)
    titulo=models.CharField(default="titulo", max_length=300,blank=True, editable=True)
    contenido=models.TextField(default="detalles",  blank=True)
    fechaPublicacion=models.DateTimeField( default=timezone.now)

class Evento(models.Model):
    foto=models.ImageField(upload_to="images/%y%m%d",null=True,blank=True)
    titulo=models.CharField(default="titulo", max_length=300,blank=True, editable=True)
    contenido=models.TextField(default="detalles",  blank=True)
    fechaPublicacion=models.DateTimeField( default=timezone.now)


class ImagenesGaleria(models.Model):
    foto=models.ImageField(upload_to="galeria/%y%m%d", null=True, blank=True)
    titulo=models.CharField(default="titulo", max_length=300,blank=True, editable=True)
    fechaPublicacion=models.DateTimeField( default=timezone.now)