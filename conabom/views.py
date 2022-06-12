
from conabom.forms import SocioForm
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from conabom.forms import CustomUserCreationForm
from conabom.models import Slider

# Create your views here.

#index
def inicio(request):
    
    obj = Slider.objects.all()
    context={ 
        'obj':obj 
        }


    return render(request, "index.html", context) 


#registro de usuarios
def registro(request):
    data= {
        'form':CustomUserCreationForm()
        }
    
    if request.method=="POST":
        formulario= CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            
            user = formulario.save()
            login(request, user)
            messages.success(request, "te has registrado correctamente")
            return redirect(to='login')
        data["form"]=formulario
    
    
    return render(request, "registration/register.html", data )


@login_required
def userIndex(request):
    return render(request, "users/user_index.html") 



@login_required
def userApplication(request):
    data={

        'form': SocioForm()
    }

    return render(request, 'users/user_application1.html', data)