from django.contrib import admin
from .models import equipos_laptop, equipos_desktops, equipos_telefono, equipos_monitor, equipos_docking, equipos_tablet, equipos_mini_pc, equipos_handheld

class EquiposAdminBase(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'serial')  # Mostrar marca, modelo y serial
    ordering = ('modelo',)  # Ordenar por 'modelo' en orden ascendente

class EquiposLaptopAdmin(EquiposAdminBase):
    pass

class EquiposDesktopsAdmin(EquiposAdminBase):
    pass

class EquiposTelefonoAdmin(EquiposAdminBase):
    pass

class EquiposMonitorAdmin(EquiposAdminBase):
    pass

class EquiposDockingAdmin(EquiposAdminBase):
    pass

class EquiposTabletAdmin(EquiposAdminBase):
    pass

class EquiposMiniPCAdmin(EquiposAdminBase):
    pass

class EquiposHandHeldAdmin(EquiposAdminBase):
    list_display = ('marca', 'modelo', 'serial')  # Mostrar marca, modelo y serial
    ordering = ('modelo', 'serial')  # Ordenar por 'modelo' en orden ascendente

admin.site.register(equipos_laptop, EquiposLaptopAdmin)
admin.site.register(equipos_desktops, EquiposDesktopsAdmin)
admin.site.register(equipos_telefono, EquiposTelefonoAdmin)
admin.site.register(equipos_monitor, EquiposMonitorAdmin)
admin.site.register(equipos_docking, EquiposDockingAdmin)
admin.site.register(equipos_tablet, EquiposTabletAdmin)
admin.site.register(equipos_mini_pc, EquiposMiniPCAdmin)
admin.site.register(equipos_handheld, EquiposHandHeldAdmin)
