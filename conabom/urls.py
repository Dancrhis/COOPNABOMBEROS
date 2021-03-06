from django.contrib import admin
from django.urls import path
from conabom import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('', views.inicio, name='index'),
    path('historia/', views.historia, name='historia'),
    path('mision_vision_valores/', views.mision, name='misionVisionValores'),
    path('ahorros/', views.ahorros, name='ahorros'),
    path('prestamos/', views.prestamos, name='prestamos'),
    path('planAyudaMutua/', views.planAyudaMutua, name='ayudaMutua'),
    path('user_index/', views.userIndex, name='userIndex'),
    path('register/', views.registro, name='register'),
    path('accounts/password_change/', views.change_password, name='passwordChange'),
    path('noticias/', views.noticiasIndex, name='noticias'),
    path('noticias/noticiaDetalles/<int:pk>', views.noticiaDetalles, name='noticiaDetalles'),
    path('eventos_Actividades/', views.eventosActividadesIndex, name='eventos'),
    path('eventos_Actividades/eventoDetalles/<int:pk>', views.EventoActividad_detalles, name='eventoDetalles'),
    path('galeria/', views.galeria, name='galeria'),
    path('accounts/user_index/userAplication/', views.userApplication, name='userApplication'),
    path('accounts/user_index/userAplication2/', views.userApplication2, name='userApplication2'),
    path('accounts/ logout/', views.logout, name='logout'),
    path('user_index/delete_beneficiario/<int:pk>', views.beneficiario_delete, name='deleteBeneficiario'),
    path('user_index/update_beneficiario/<int:pk>', views.beneficiario_update, name='updateBeneficiario'),
    path('user_index/update_socio/<str:pk>', views.socio_update, name='updateSocio'),
    
]

        