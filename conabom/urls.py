from django.contrib import admin
from django.urls import path
from conabom import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('', views.inicio, name='index'),
    path('historia/', views.historia, name='historia'),
    path('mision/', views.mision, name='mision'),
    path('user_index/', views.userIndex, name='userIndex'),
    path('register/', views.registro, name='register'),
    path('noticias/', views.noticiasIndex, name='noticias'),
    path('noticias/noticiaDetalles/<int:pk>', views.noticiaDetalles, name='noticiaDetalles'),
    path('accounts/user_index/userAplication/', views.userApplication, name='userApplication'),
    path('accounts/user_index/userAplication2/', views.userApplication2, name='userApplication2'),
    path('accounts/ logout/', views.logout, name='logout'),
    path('user_index/delete_beneficiario/<int:pk>', views.beneficiario_delete, name='deleteBeneficiario'),
    path('user_index/update_beneficiario/<int:pk>', views.beneficiario_update, name='updateBeneficiario'),
    path('user_index/update_socio/<str:pk>', views.socio_update, name='updateSocio'),
    
]

        