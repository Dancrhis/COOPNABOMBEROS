from django.contrib import admin

from conabom.models import Beneficiario, Evento, Noticia, Socio,Slider


# Register your models here.

class SocioAdmin(admin.ModelAdmin):
    list_display= ["estado","nombre1","nombre2","apellido1","apellido2","cedula","telefono","celular"]
    list_filter= ["fechaSolicitud", "estado"]
    search_fields=["nombre1","nombre2","apellido1","apellido2","cedula","telefono","celular"]


class BeneficiarioAdmin(admin.ModelAdmin):
    list_display= ["afiliado","nombre1","nombre2","apellido1","apellido2","cedula","telefono","parentezco","porcentaje"]
    list_filter= ["afiliado"]
    search_fields=["nombre1","nombre2","apellido1","apellido2","cedula","telefono",]

class NoticiaAdmin(admin.ModelAdmin):
    list_display= ["titulo","fechaPublicacion"]
    list_filter= ["fechaPublicacion"]
    search_fields=["titulo"]

class EventoAdmin(admin.ModelAdmin):
    list_display= ["titulo","fechaPublicacion"]
    list_filter= ["fechaPublicacion"]
    search_fields=["titulo"]


admin.site.register(Socio, SocioAdmin)
admin.site.register(Beneficiario,BeneficiarioAdmin)
admin.site.register(Noticia,NoticiaAdmin)
admin.site.register(Evento, EventoAdmin)