from django.shortcuts import render
from .models import ALMACENES, equipos_laptop, equipos_telefono, equipos_monitor, equipos_docking, equipos_tablet, equipos_mini_pc, equipos_desktops, equipos_handheld

def almacen_equipos(request):
    almacen = ALMACENES.objects.all()
    computadora = equipos_laptop.objects.all().order_by('modelo')
    phone = equipos_telefono.objects.all().order_by('modelo')
    pantalla = equipos_monitor.objects.all().order_by('modelo')
    dock = equipos_docking.objects.all().order_by('modelo')
    tableta = equipos_tablet.objects.all().order_by('modelo')
    little_pc = equipos_mini_pc.objects.all().order_by('modelo')
    desktopp = equipos_desktops.objects.all().order_by('modelo')
    hh = equipos_handheld.objects.all().order_by('sucursal')
    context = {
        'computadoras': computadora,
        'phones': phone,
        'pantallas': pantalla,
        'docks': dock,
        'tabletas': tableta,
        'little_pcs': little_pc,
        'desktopps': desktopp,
        'hhs': hh,
        'almacens': almacen,
    }
    return render(request, 'personal/templates/inventario.html', context)