




from django.forms import  DateInput, HiddenInput, ModelForm, NumberInput, RadioSelect, Select, TextInput
from django.contrib.auth.forms import UserCreationForm

from conabom.models import Beneficiario, Socio
from django.contrib.auth.models import User




class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

class SocioForm(ModelForm):
    
    class Meta :
        
        CIVILCHOICES=[('soltero','soltero/a'),
                    ('casado','casado/a'),
                    ('union libre','union libre'),
                    ('viudo','viudo/a'),]
        SEXOCHOICES=[('M','Masculino'),
                    ('F','Femenino')]
        IAECHOICES=[('Cuerpo de Bomberos ','Cuerpo de Bomberos'),
                    ('Policia Municipal ','Policia Municipal'),
                    ('Centro Especializado Comunitario(C.E.C) ','Centro Especializado Comunitario(C.E.C)'),
                    ('Patronato Nacional de Seguridad Ciudadana','Patronato Nacional de Seguridad Ciudadana'),
                    ('Academia Nacional de seguridad y Apoyo Hospitalario (ANSAH) ','Academia Nacional de seguridad y Apoyo Hospitalario (ANSAH)'),
                    ('Cruz Roja','Cruz Roja'),
                    ('Defensa Civil','Defensa Civil'),
                    ('OTRA','OTRA'),]
        model = Socio
        fields= ['usuario',
                'estado',
                'nombre1',
                'nombre2',
                'apellido1',
                'apellido2',
                'nacionalidad',
                'cedula',
                'fechaNacimiento',
                'sexo',
                'provincia',
                'municipio',
                'sector',
                'estadoCivil',
                'celular',
                'telefono',
                'lugarTrabajo',
                'cargo',
                'telefonoLugarTrabajo',
                'banco',
                'numeroCuenta',
                'institucionAtencionEmergencia',
                'ubicacion',
                'aporte'
                ]

        widgets={
            'nombre2': TextInput(attrs={'required': False, 'blank': False}, ),
            'apellido2': TextInput(attrs={'required': False, 'blank': False}),
            'telefono': NumberInput(attrs={'required': False, 'blank': False}),
            'fechaNacimiento': DateInput(attrs={'type':"date"}),
            'sexo': Select(choices=SEXOCHOICES),
            'estadoCivil': Select(choices=CIVILCHOICES),
            'estado':HiddenInput(attrs={'value': "registro2"}),
            'usuario':HiddenInput(),
            'institucionAtencionEmergencia': Select(choices=IAECHOICES),
            
        }
        labels = {
            'nombre1': ("Nombre"),
            'nombre2':("Segundo nombre"),
            'apellido1':("Aplellido"),
            'apellido2':("Segundo apellido"),
            'cedula':("Identificacion(cedula/pasaporte)"),
            'fechaNacimiento' :("Fecha de Nacimiento"),
            'nacionalidad':("Nacionalidad"),
            'sexo':("Sexo"),
            'provincia':("Provincia"),
            'municipio':("Municipio"),
            'sector':("Sector"),
            'estadoCivil':("Estado civil:"),
            'celular':("Celular:"), 
            'telefono':("Telefono:"),
            'lugarTrabajo':("Lugar de Trabajo:"),
            'cargo':("Cargo que desempeña:"),
            'telefonoLugarTrabajo':("Telefono del trabajo:"),
            'institucionAtencionEmergencia':("Institucion de atencion a emergecias:"),
            'ubicacion':("De:"),
            'aporte':("Aporte: "),
        }

class BeneficiarioForms(ModelForm):
    class Meta :
        PARENTCHOICES=[('Padre','Madre'),
                       ('Padre','Padre'),
                       ('Hermano/a','Hermano/a'),
                       ('Hijo/a','hija/a'),
                       ('Esposo/a','Esposo/a'),
                       ('Primo/a','Primo/a'),
                       ('Tio/a','Tio/a'),
                       ('Abuelo/a','Abuelo/a'),]
        model=Beneficiario
        fields=['cedula', 'afiliado','nombre1', 'nombre2','apellido1','apellido2','parentezco','porcentaje','telefono']
        labels = {

            'nombre1': ("Nombre: "),
            'nombre2':("Segundo nombre: "),
            'apellido1':("Apellido: "),
            'apellido2':("Segundo apellido: "),
            'cedula':("Cedula: "),
            'parentezco':("Parentezco: "),
            'porcentaje':("Porcentaje: "),
            'telefono':("Telefono: "),
            'afiliado': ("Afiliado: ")
            }
        widgets={
            'afiliado':HiddenInput(),
            'nombre2': TextInput(attrs={'required': False, 'blank': False}),
            'apellido2': TextInput(attrs={'required': False, 'blank': False}),
            'parentezco': Select(choices=PARENTCHOICES),
            
            
        }    