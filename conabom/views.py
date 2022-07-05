

from conabom.forms import BeneficiarioForms, SocioForm
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from conabom.forms import CustomUserCreationForm
from conabom.models import Beneficiario, Slider, Socio, Noticia, Evento
from django.core.paginator import Paginator

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

#noticia
def noticiaDetalles(request,pk):
    noticia=Noticia.objects.get(pk=pk)

    context={
        'noticia': noticia,
    }
    return render(request, 'noticia.html', context)

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

def noticiasIndex(request):
    noticias =Noticia.objects.all().order_by("-fechaPublicacion")
    noticias_page=Paginator(noticias,10)
    page_number = request.GET.get('page')
    page_obj= noticias_page.get_page(page_number)
    context={
        'page_obj': page_obj,
    }
    return render(request,"noticias.html", context)


@login_required
def userIndex(request):
    
    data={
        'user_info':Socio.objects.filter(usuario=request.user),
        'beneficiario_info': Beneficiario.objects.filter(afiliado=request.user)
    }
    return render(request, "users/user_index.html", data) 



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
            
            data={
                'form': BeneficiarioForms()
            }
            return render(request, 'users/user_application2.html', data)
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
    data={
        'form': BeneficiarioForms()
    }
    if request.method=="POST":
        beneficiario= BeneficiarioForms(data=request.POST)
        print(beneficiario.is_valid())
        for field in beneficiario:
            print("Field Error:", field.name,  field.errors)
        
        if beneficiario.is_valid():
            
            
            beneficiario.save()
            return redirect(to='userIndex')
        else:
            data={

                'form': beneficiario
                }
            
            return render(request, 'users/user_application2.html', data)

    return render(request, 'users/user_application2.html', data)

@login_required
def beneficiario_update(request, pk):
    bene=Beneficiario.objects.get(id=pk)

    if request.method =='POST':
        form = BeneficiarioForms(request.POST, instance = bene)
        if form.is_valid():
            form.save()

            return redirect( to='userIndex')
    else:
        form = BeneficiarioForms(instance=bene)

    return render(request,'users/beneficiario_update.html',{'form': form} )
        
            


@login_required
def beneficiario_delete(request, pk):
    esteBeneficiario=Beneficiario.objects.get(id=pk)
    esteBeneficiario.delete()
    

    return redirect(to='userIndex' )