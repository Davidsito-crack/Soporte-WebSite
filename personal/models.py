import os
from django.core.exceptions import ValidationError
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete
from inventario.models import equipos_laptop, equipos_telefono, equipos_monitor, equipos_docking, equipos_tablet, equipos_mini_pc, equipos_handheld, equipos_desktops

class people(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    apellido = models.CharField(max_length=100, null=False, blank=False)
    numero_de_empleado = models.CharField(max_length=4, null=False, blank=False, unique=True)
    puesto = models.CharField(max_length=100, null=False, blank=False)
    numero_de_telefono = models.CharField(max_length=15, null=True, blank=True)
    SUCURSALES_OPT = (
        ('Chihuahua', 'Chihuahua'),
        ('Juárez', 'Juárez'),
        ('Guaymas', 'Guaymas'),
        ('Monterrey', 'Monterrey'),
        ('Tamaulipas', 'Tamaulipas'),
        ('Querétaro', 'Querétaro'),
        ('Mexicali', 'Mexicali'),
        ('Silao', 'Silao'),
        ('Guanajuato', 'Guanajuato'),
        ('CDMX', 'CDMX'),
        ('Tijuana', 'Tijuana'),
        ('Guadalajara', 'Guadalajara'),
    )
    sucursal = models.CharField(max_length=25, choices=SUCURSALES_OPT, null=False, blank=False, default="...")
    correo = models.CharField(max_length=100, default='@mscdirect.com.mx', blank=True, null=True)
    VPN = models.CharField(max_length=20, blank=True, null=True)
    
    # Aquí daremos de opciones para cada tipo de equipo los equipos que actualmente fueron registrados individualmente
    laptop = models.ForeignKey(equipos_laptop, null=True, blank=True, on_delete=models.CASCADE, unique=True)
    telefono = models.ForeignKey(equipos_telefono, null=True, blank=True, on_delete=models.CASCADE, unique=True)
    monitor = models.ForeignKey(equipos_monitor, null=True, blank=True, on_delete=models.CASCADE, unique=True)
    docking = models.ForeignKey(equipos_docking, null=True, blank=True, on_delete=models.CASCADE, unique=True)
    tablet = models.ForeignKey(equipos_tablet, null=True, blank=True, on_delete=models.CASCADE, unique=True)
    mini_pc = models.ForeignKey(equipos_mini_pc, null=True, blank=True, on_delete=models.CASCADE, unique=True)
    hand_held = models.ForeignKey(equipos_handheld, null=True, blank=True, on_delete=models.CASCADE, unique=True)
    desktop = models.ForeignKey(equipos_desktops, null=True, blank=True, on_delete=models.CASCADE, unique=True)
    
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.nombre}, {self.puesto}"
    
    def clean(self):
        super().clean()
        # Validación de espacios en campos
        if ' ' in self.numero_de_empleado:
            raise ValidationError({'numero_de_empleado': 'El número de empleado no puede contener espacios.'})
        if self.numero_de_telefono and ' ' in self.numero_de_telefono:
            raise ValidationError({'numero_de_telefono': 'El número de teléfono no puede contener espacios.'})
        
        # Validaciones de sucursal
        if self.laptop and self.laptop.sucursal != self.sucursal:
            raise ValidationError(f"La laptop asignada debe estar en la misma sucursal que la persona ({self.sucursal}).")
        if self.telefono and self.telefono.sucursal != self.sucursal:
            raise ValidationError(f"El teléfono asignado debe estar en la misma sucursal que la persona ({self.sucursal}).")
        if self.monitor and self.monitor.sucursal != self.sucursal:
            raise ValidationError(f"El monitor asignado debe estar en la misma sucursal que la persona ({self.sucursal}).")
        if self.docking and self.docking.sucursal != self.sucursal:
            raise ValidationError(f"El docking station asignado debe estar en la misma sucursal que la persona ({self.sucursal}).")
        if self.tablet and self.tablet.sucursal != self.sucursal:
            raise ValidationError(f"La tablet asignada debe estar en la misma sucursal que la persona ({self.sucursal}).")
        if self.mini_pc and self.mini_pc.sucursal != self.sucursal:
            raise ValidationError(f"La mini PC asignada debe estar en la misma sucursal que la persona ({self.sucursal}).")
        if self.hand_held and self.hand_held.sucursal != self.sucursal:
            raise ValidationError(f"La HandHeld asignada debe estar en la misma sucursal que la persona ({self.sucursal}).")
        if self.desktop and self.desktop.sucursal != self.sucursal:
            raise ValidationError(f"El desktop asignado debe estar en la misma sucursal que la persona ({self.sucursal}).")
    
    def save(self, *args, **kwargs):
        self.clean()  # Llama al método clean() para validar antes de guardar
        super().save(*args, **kwargs)
        
class comodatos(models.Model):
    comodatario = models.ForeignKey(people, on_delete=models.CASCADE)
    comodato = models.FileField(upload_to='Documents/')
    fecha_de_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comodatario.nombre} {self.comodatario.apellido}. Fecha: {self.fecha_de_subida}"

@receiver(post_delete, sender=comodatos)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Elimina el archivo del sistema de archivos
    cuando se elimina el objeto `comodatos` correspondiente.
    """
    if instance.comodato:
        if os.path.isfile(instance.comodato.path):
            os.remove(instance.comodato.path)

class sucursals(models.Model):
    titulo = models.CharField(max_length=50, null=False, blank=False)
    SUCURSALES_OPT = (
        ('Chihuahua', 'Chihuahua'),
        ('Juárez', 'Juárez'),
        ('Guaymas', 'Guaymas'),
        ('Monterrey', 'Monterrey'),
        ('Tamaulipas', 'Tamaulipas'),
        ('Querétaro', 'Querétaro'),
        ('Mexicali', 'Mexicali'),
        ('Silao', 'Silao'),
        ('Guanajuato', 'Guanajuato'),
        ('CDMX', 'CDMX'),
        ('Tijuana', 'Tijuana'),
        ('Guadalajara', 'Guadalajara'),
    )
    sucursal = models.CharField(max_length=25, choices=SUCURSALES_OPT, null=False, blank=False, default="Chihuahua")
    
    laptop = models.ForeignKey(equipos_laptop, null=True, blank=True, on_delete=models.CASCADE, unique=True)
    telefono = models.ForeignKey(equipos_telefono, null=True, blank=True, on_delete=models.CASCADE, unique=True)
    monitor = models.ForeignKey(equipos_monitor, null=True, blank=True, on_delete=models.CASCADE, unique=True)
    docking = models.ForeignKey(equipos_docking, null=True, blank=True, on_delete=models.CASCADE, unique=True)
    tablet = models.ForeignKey(equipos_tablet, null=True, blank=True, on_delete=models.CASCADE, unique=True)
    mini_pc = models.ForeignKey(equipos_mini_pc, null=True, blank=True, on_delete=models.CASCADE, unique=True)
    hand_held = models.ForeignKey(equipos_handheld, null=True, blank=True, on_delete=models.CASCADE, unique=True)
    desktop = models.ForeignKey(equipos_desktops, null=True, blank=True, on_delete=models.CASCADE, unique=True)
    
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.titulo}, {self.sucursal}."