from django.contrib import admin
from django import forms
from .models import people, comodatos, sucursals

class PeopleAdmin(admin.ModelAdmin):
    model = people
    list_display = ('nombre', 'apellido', 'numero_de_empleado', 'sucursal', 'is_active')  # Mostrar el estado de actividad
    actions = ['make_inactive']
    ordering = ('nombre',)  # Orden descendente por el campo 'nombre'
    
    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
    make_inactive.short_description = "Inhabilitar a las personas seleccionadas"

admin.site.register(people, PeopleAdmin)

# Nueva clase para personalizar la visualización de los comodatos
class ComodatosAdmin(admin.ModelAdmin):
    list_display = ('get_nombre', 'get_apellido', 'fecha_de_subida')  # Campos que se mostrarán en la lista
    ordering = ('comodatario__nombre',)  # Ordenar por el nombre del comodatario

    # Función para obtener el nombre del comodatario relacionado
    def get_nombre(self, obj):
        return obj.comodatario.nombre
    get_nombre.short_description = 'Nombre'
    get_nombre.admin_order_field = 'comodatario__nombre'  # Permite ordenar por el nombre

    # Función para obtener el apellido del comodatario relacionado
    def get_apellido(self, obj):
        return obj.comodatario.apellido
    get_apellido.short_description = 'Apellido'
    get_apellido.admin_order_field = 'comodatario__apellido'  # Permite ordenar por el apellido

admin.site.register(comodatos, ComodatosAdmin)

class SucursalsAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'sucursal', 'is_active')
    actions = ['make_inactive', 'make_active']
    ordering = ('titulo',)
    
    # Método opcional para personalizar la visualización
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # Puedes agregar lógica aquí si es necesario
        return queryset
    
    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
        
    def make_active(self, request, queryset):
        queryset.update(is_active=True)
        
    make_inactive.short_description = "Inhabilitar a los seleccionados"
    make_active.short_description = "Habilitad seleccionados"
admin.site.register(sucursals, SucursalsAdmin)
