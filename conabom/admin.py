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
admin.site.register(Socio, SocioAdmin)
admin.site.register(Beneficiario,BeneficiarioAdmin)
admin.site.register(Slider)
admin.site.register(Noticia)
admin.site.register(Evento)