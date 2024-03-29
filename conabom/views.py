

from itertools import count
from conabom.forms import BeneficiarioForms, SocioForm
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login
from conabom.forms import CustomUserCreationForm
from conabom.models import Beneficiario, ImagenesGaleria, Slider, Socio, Noticia, Evento
from django.core.paginator import Paginator
from django.contrib.auth import update_session_auth_hash
# Create your views here.

#index
def inicio(request):
    
    obj = Evento.objects.all().order_by('-fechaPublicacion')
    obj2 = Noticia.objects.all().order_by('-fechaPublicacion')
    context={ 
        'evento1':obj[0],
        'evento2':obj[1],
        'evento3':obj[2],
        'noticia1':obj2[0],
        'noticia2':obj2[1],
        'noticia3':obj2[2],
        'noticia4':obj2[3],
        }


    return render(request, "index.html", context) 

def logout(request):
    return render(request, 'registration/logged_out.html')

#historia

def historia(request):
    return render(request, 'historia.html')

#mision vision valores
def mision(request):
    return render(request, 'mision_vision_valores.html')

#ahorros
def ahorros(request):
    return render(request, 'ahorros.html')

#prestamos
def prestamos(request):
    return render(request, 'prestamos.html')
#plan ayuda mutua
def planAyudaMutua(request):
    return render(request, 'PlanAyudaMutua.html')
#noticia

def noticiasIndex(request):
    noticias =Noticia.objects.all().order_by("-fechaPublicacion")
    noticias_page=Paginator(noticias,10)
    page_number = request.GET.get('page')
    page_obj= noticias_page.get_page(page_number)
    context={
        'page_obj': page_obj,
    }
    return render(request,"noticias.html", context)  

#noticiaDetalles
def noticiaDetalles(request,pk):
    noticia=Noticia.objects.get(pk=pk)

    context={
        'noticia': noticia,
    }
    return render(request, 'noticia.html', context)


#eventos

def eventosActividadesIndex(request):
    eventos =Evento.objects.all().order_by("-fechaPublicacion")
    eventos_page=Paginator(eventos,10)
    page_number = request.GET.get('page')
    page_obj= eventos_page.get_page(page_number)
    context={
        'page_obj': page_obj,
    }
    return render(request,"eventos_actividades.html", context)  

#evento_detalles
def EventoActividad_detalles(request,pk):
    evento=Evento.objects.get(pk=pk)

    context={
        'evento': evento,
    }
    return render(request, 'evento.html', context)


#eventos

def galeria(request):
    imagenes =ImagenesGaleria.objects.all().order_by("-fechaPublicacion")
    imagenes_page=Paginator(imagenes,10)
    page_number = request.GET.get('page')
    page_obj= imagenes_page.get_page(page_number)
    context={
        'page_obj': page_obj,
    }
    return render(request,"galeria.html", context)
#registro de usuarios
def registro(request):
    data= {
        'form':CustomUserCreationForm()
        }
    
    if request.method=="POST":
        formulario= CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            try:

                user = formulario.save()
                login(request, user)
                messages.success(request, "te has registrado correctamente")
                return redirect(to='userIndex')
            except:
                return render(request,'register',{'msj':'el nombre de usuario ya existe', 'form':formulario})

            
        data["form"]=formulario
    
    
    return render(request, "registration/register.html", data )


@login_required
def userIndex(request):
    ucounter=0
    bcounter=0
    for n in Socio.objects.filter(usuario=request.user):
        ucounter =+1

    bcounter=0
    for n in Beneficiario.objects.filter(afiliado=request.user):
        bcounter =+1
    
    data={
        'user_info':Socio.objects.filter(usuario=request.user),
        'beneficiario_info': Beneficiario.objects.filter(afiliado=request.user),
        'user_cantidad': ucounter,
        'bene_cantidad': bcounter,
    }
    print(bcounter)

    return render(request, "users/user_index.html", data) 

#cambio de contraseña
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'se ha actualizado tu Contraseña!')
            return redirect('login')
        else:
            messages.error(request, 'por favor corrija los siguientes errores:')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/user_password_change.html', {
        'form': form
    })

@login_required
def userApplication(request):
    
    data={

        'form': SocioForm()
    }
    if request.method=="POST":
        socio= SocioForm(data=request.POST)
        print(socio.is_valid())
        for field in socio:
            print("Field Error:", field.name,  field.errors)
        
        if socio.is_valid():
            
            
            socio.save()
            
            
            return redirect(to= 'userIndex')
        else:
            data={

                'form': socio
                }
            
            return render(request, 'users/user_application1.html', data)
    
    
   

    return render(request, 'users/user_application1.html', data)


@login_required
def socio_update(request, pk):
    afiliado=Socio.objects.get(usuario=pk)

    if request.method =='POST':
        form = SocioForm(request.POST, instance = afiliado)
        if form.is_valid():
            form.save()

            return redirect( to='userIndex')
    else:
        form = SocioForm(instance=afiliado)

    return render(request,'users/user_application1.html',{'form': form} )




@login_required
def userApplication2(request):
    benep=Beneficiario.objects.all().filter(afiliado=request.user)
    porciento=0

    for benef in benep:
        porciento+=benef.porcentaje
    data={
        'form': BeneficiarioForms(),
        'porciento':porciento
    }
    if request.method=="POST":
        
        beneficiario= BeneficiarioForms(data=request.POST)
        
        postPorciento=int(request.POST['porcentaje'])
        porciento+=postPorciento
        if beneficiario.is_valid() and porciento<101:
            
            
            beneficiario.save()
            return redirect(to='userIndex')
        else:
            if porciento>100:
                data={

                    'form': beneficiario,
                    'message': "no puede exceder el 100%",
                    'porciento':porciento
                    }
                
                return render(request, 'users/user_application2.html', data)
            else:
                data={

                    'form': beneficiario,
                    }
                return render(request, 'users/user_application2.html', data)


    return render(request, 'users/user_application2.html', data)

@login_required
def beneficiario_update(request, pk):
    bene=Beneficiario.objects.get(id=pk)
    benep=Beneficiario.objects.all().filter(afiliado=request.user)
    porciento=0
    for benef in benep:
        porciento+=benef.porcentaje
    
        
    if request.method =='POST': 
        postPorciento=int(request.POST['porcentaje'])
        porciento+=postPorciento
        porciento-=bene.porcentaje
        form = BeneficiarioForms(request.POST, instance = bene)
        if form.is_valid()and porciento<101:
            form.save()

            return redirect( to='userIndex')
    else:
        form = BeneficiarioForms(instance=bene)

    return render(request,'users/beneficiario_update.html',{'form': form, 'porciento':porciento} )
        
            


@login_required
def beneficiario_delete(request, pk):
    esteBeneficiario=Beneficiario.objects.get(id=pk)
    esteBeneficiario.delete()
    

    return redirect(to='userIndex' )