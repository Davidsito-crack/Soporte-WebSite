from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import FileResponse
from django.contrib import messages
from .models import people, comodatos, sucursals
from .forms import comodatosForm
from django.utils import timezone
from django.http import JsonResponse
from inventario.models import equipos_laptop, equipos_telefono, equipos_monitor, equipos_docking, equipos_tablet, equipos_mini_pc, equipos_desktops, equipos_handheld

def asignar_equipo(request, equipo_id, persona_id, equipo_tipo):
    equipo = None
    if equipo_tipo == 'laptop':
        equipo = equipos_laptop.objects.get(id=equipo_id)
    elif equipo_tipo == 'telefono':
        equipo = equipos_telefono.objects.get(id=equipo_id)
    elif equipo_tipo == 'monitor':
        equipo = equipos_monitor.objects.get(id=equipo_id)
    elif equipo_tipo == 'docking':
        equipo = equipos_docking.objects.get(id=equipo_id)
    elif equipo_tipo == 'tablet':
        equipo = equipos_tablet.objects.get(id=equipo_id)
    elif equipo_tipo == 'mini_pc':
        equipo = equipos_mini_pc.objects.get(id=equipo_id)
    elif equipo_tipo == 'desktop':
        equipo = equipos_desktops.objects.get(id=equipo_id)
    elif equipo_tipo == 'handheld':
        equipo = equipos_handheld.objects.get(id=equipo_id)
    
    persona = people.objects.get(id=persona_id)
    
    if equipo.sucursal != persona.sucursal:
        messages.error(request, "El equipo y la persona asignada deben pertenecer a la misma sucursal.")
        return redirect('equipos_view')
    
    equipo.asignado = persona
    equipo.save()
    messages.success(request, "Equipo asignado correctamente.")
    return redirect('equipos_view')

def inventarios_view(request):
    gente = people.objects.all().order_by('nombre')
    return render(request, 'info.html', {'gentes': gente})

def inicio_view(request):
    return render(request, 'inicio.html')

def equipos_view(request):
    computadora = equipos_laptop.objects.all().order_by('modelo')
    phone = equipos_telefono.objects.all().order_by('modelo')
    pantalla = equipos_monitor.objects.all().order_by('modelo')
    dock = equipos_docking.objects.all().order_by('modelo')
    tableta = equipos_tablet.objects.all().order_by('modelo')
    little_pc = equipos_mini_pc.objects.all().order_by('modelo')
    desktopp = equipos_desktops.objects.all().order_by('modelo')
    hh = equipos_handheld.objects.all().order_by('sucursal', 'modelo')
    sucursal = sucursals.objects.all().order_by('sucursal')
    gente = people.objects.all()
    gentuza = sucursals.objects.all()
    
    for comp in computadora:
        comp.asignado = any(persona.laptop == comp for persona in gente)
        
    for phonky in phone:
        phonky.asignado = any(persona.telefono == phonky for persona in gente)
    
    for pantallon in pantalla:
        pantallon.asignado = any(persona.monitor == pantallon for persona in gente)
    
    for docky in dock:
        docky.asignado = any(persona.docking == docky for persona in gente)
    
    for tablets in tableta:
        tablets.asignado = any(persona.tablet == tablets for persona in gente)
    
    for little_PC in little_pc:
        little_PC.asignado = any(persona.mini_pc == little_PC for persona in gente)
        
    for DESK in desktopp:
        DESK.asignado = any(persona.desktop == DESK for persona in gente)
        
    for HANDHELD in hh:
        HANDHELD.asignado = any(persona.hand_held == HANDHELD for persona in gente)
                
    context = {
        'computadoras': computadora,
        'phones': phone,
        'pantallas': pantalla,
        'docks': dock,
        'tabletas': tableta,
        'little_pcs': little_pc,
        'desktopps': desktopp,
        'hhs': hh,
        'sucursals': sucursal,
        'gentuzas': gentuza,
        'gentes': gente,
    } 
    
    return render(request, 'inventario.html', context)

def comodatos_view(request):
    personas = people.objects.all().order_by('nombre')  # Ordenar por nombre en orden descendente

    if request.method == 'POST':
        form = comodatosForm(request.POST, request.FILES)
        if form.is_valid():
            comodatario = form.cleaned_data['comodatario']
            # Eliminar documentos antiguos del comodatario
            comodatos.objects.filter(comodatario=comodatario).delete()
            form.save()
            messages.success(request, "Documento subido correctamente.")
            return redirect('comodatos')
    else:
        form = comodatosForm()

    # Obtener documentos filtrados por comodatario seleccionado si hay filtro
    persona_id = request.GET.get('persona_id')
    if persona_id:
        # Ordenar los documentos por el nombre del comodatario
        documentos = comodatos.objects.filter(comodatario__id=persona_id).order_by('comodatario__nombre')
    else:
        # Obtener todos los documentos y ordenar por nombre del comodatario
        documentos = comodatos.objects.all().order_by('comodatario__nombre')

    return render(request, 'comodatos.html', {'form': form, 'documentos': documentos, 'personas': personas})

def upload_document(request):
    if request.method == 'POST':
        comodatario_id = request.POST.get('comodatario_id')
        comodatario = get_object_or_404(people, pk=comodatario_id)
        
        form = comodatosForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                comodato = form.save(commit=False)
                comodato.comodatario = comodatario
                
                # Verificar si ya existe un documento para este comodatario y eliminarlo
                existing_documents = comodatos.objects.filter(comodatario=comodatario)
                if existing_documents.exists():
                    existing_documents.delete()
                
                comodato.save()
                messages.success(request, "Documento subido correctamente.")
                return redirect('comodatos')  # Redireccionar a la página comodatos
            except Exception as e:
                print(e)
                return JsonResponse({'success': False, 'message': 'Error al guardar el documento.'})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors})
    else:
        return JsonResponse({'success': False, 'message': 'Método no permitido'})

def view_document(request, document_id):
    document = get_object_or_404(comodatos, id=document_id)
    return FileResponse(document.comodato.open(), as_attachment=False)

def download_document(request, document_id):
    document = get_object_or_404(comodatos, id=document_id)
    return FileResponse(document.comodato.open(), as_attachment=True)

def delete_document(request, document_id):
    documento = get_object_or_404(comodatos, id=document_id)
    
    if request.method == 'POST':
        documento.delete()
        messages.success(request, "Documento eliminado correctamente.")
    else:
        messages.error(request, "Error al intentar eliminar el documento.")
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'comodatos'))


def person_info_view(request, person_id):
    try:
        persona = people.objects.get(id=person_id)
        data = {
            'id': persona.id,
            'nombre': persona.nombre,
            'sucursal': persona.sucursal,
            'telefono': persona.telefono,
            # Añade más campos según sea necesario
        }
        return JsonResponse(data)
    except people.DoesNotExist:
        return JsonResponse({'error': 'Persona no encontrada'}, status=404)