from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.inventarios_view, name='informacion'),
    path('inicio/', views.inicio_view, name='inicio'),
    path('equipos/', views.equipos_view, name='equipos'),
    path('comodatos/', views.comodatos_view, name='comodatos'),
    path('upload_document/', views.upload_document, name='upload_document'),
    path('person-info/<int:person_id>/', views.person_info_view, name='person_info'),
    path('delete_document/<int:document_id>/', views.delete_document, name='delete_document'),
]

