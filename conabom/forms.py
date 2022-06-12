

from django.forms import DateInput, ModelForm

from django.contrib.auth.forms import UserCreationForm
from conabom.models import Socio
from django.contrib.auth.models import User




class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

class SocioForm(ModelForm):
    class Meta :
        model = Socio
        fields= ['nombre1' ,'nombre2','apellido1','apellido2','cedula','fechaNacimiento','sexo','provincia','municipio','sector','estadoCivil', 'telefono','lugarTrabajo','cargo', 'telefonoLugarTrabajo']
        widgets={
            'fechaNacimiento': DateInput(attrs={'type':"date"}),
            
        }
        labels = {
            'nombre1': ("Nombre"),
            'nombre2':("Segundo nombre"),
            'apellido1':("Aplellido"),
            'apellido2':("Segundo apellido"),
            'cedula':("Identificacion(cedula/pasaporte)"),
            'fechaNacimiento' :("Fecha de Nacimiento"),
            'sexo':("Sexo"),
            'provincia':("Provincia"),
            'municipio':("Municipio"),
            'sector':("Sector"),
            'estadoCivil':("Estado civil:"), 
            'telefono':("Telefono:"),
            'lugarTrabajo':("Lugar de Trabajo:"),
            'cargo':("Cargo que desempeña:"),
             'telefonoLugarTrabajo':("Telefono del trabajo:"),
        }


