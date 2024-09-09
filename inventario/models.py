from django.db import models

# Clase donde manejaremos todos los equipos de cada usuario
class equipos_laptop(models.Model):
    
    # Opciones para agregar laptop
    MARCA_LAPTOP_OPT = (
        ('Dell', 'Dell'),
        ('Apple', 'Apple'),
        ('Microsoft', 'Microsoft'),
    )
    marca = models.CharField(max_length=9, choices=MARCA_LAPTOP_OPT, null=False, blank=False)
    
    MODELO_LAPTOP_OPT = (
        ('Latitude 3510', 'Latitude 3510'),
        ('Latitude 3520', 'Latitude 3520'),
        ('Latitude 3540', 'Latitude 3540'),
        ('Latitude 3550', 'Latitude 3550'),
        ('Inspiron 3583', 'Inspiron 3583'),
        ('Inspiron 5540', 'Inspiron 5520'),
        ('Inspiron 5530', 'Inspiron 5530'),
        ('Inspiron 5540', 'Inspiron 5540'),
        ('Inspiron 5570', 'Inspiron 5570'),
        ('Precision 7780', 'Precision 7780'),
        ('XPS 13 9350', 'XPS 13 9350'),
        ('XPS 13 9360', 'XPS 13 9360'),
        ('XPS 13 9370', 'XPS 13 9370'),
        ('XPS 13 9380', 'XPS 13 9380'),
    )
    modelo = models.CharField(max_length=15, choices=MODELO_LAPTOP_OPT)
    
    serial = models.CharField(max_length=30, null=False, blank=False, unique=True)
        
    tipo_almacenamiento = models.CharField(max_length=35, null=False, blank=False)
    
    almacenamiento = models.CharField(max_length=10, null=False, blank=False)
    
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
    sucursal = models.CharField(max_length=11, choices=SUCURSALES_OPT, null=False, blank=False, default="Chihuahua")
    
    asignado = models.BooleanField(default=False)
        
    def __str__(self):
        return f"{self.marca} {self.modelo}. Serial: {self.serial}"
    
class equipos_desktops(models.Model):
    MARCA_LAPTOP_OPT = (
        ('Dell', 'Dell'),
        ('Apple', 'Apple'),
        ('Microsoft', 'Microsoft'),
    )
    marca = models.CharField(max_length=9, choices=MARCA_LAPTOP_OPT, null=False, blank=False)
    
    modelo = models.CharField(max_length=25)
    
    serial = models.CharField(max_length=30, null=False, blank=False, unique=True)
    
    tipo_almacenamiento = models.CharField(max_length=35, null=False, blank=False)
    
    almacenamiento = models.CharField(max_length=10, null=False, blank=False)
    
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
    sucursal = models.CharField(max_length=11, choices=SUCURSALES_OPT, null=False, blank=False, default="Chihuahua")
    
    asignado = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.marca} {self.modelo}. Serial: {self.serial}"
    
class equipos_telefono(models.Model):
    ext = models.CharField(max_length=10, null=True, blank=True)
    
    # Colocamos la marca de la laptop
    MARCA_TEL_OPT = (
        ('Samsung', 'Samsung'),
        ('Apple', 'Apple'),
        ('Xiaomi', 'Xiaomi'),
        ('TCL', 'TCL'),
    )
    marca = models.CharField(max_length=7, choices=MARCA_TEL_OPT, null=False, blank=False)
    
    MODELO_TEL_OPT = (
        ('T770B', 'T770B'),
        ('Galaxy A03s', 'Galaxy A03s'),
        ('Galaxy A20s', 'Galaxy A20s'),
        ('Galaxy A33 5G', 'Galaxy A33 5G'),
        ('Galaxy A50', 'Galaxy A50'),
        ('Galaxy A51', 'Galaxy A51'),
        ('Galaxy S23 Ultra', 'Galaxy S23 Ultra'),
        ('Galaxy S23 Plus', 'Galaxy S23 Plus'),
        ('Galaxy S23', 'Galaxy S23'),
        ('Galaxy S24 Ultra', 'Galaxy S24 Ultra'),
        ('Galaxy S24 Plus', 'Galaxy S24 Plus'),
        ('Galaxy S24', 'Galaxy S24'),
        ('iPhone X', 'iPhone X'),
        ('iPhone XS', 'iPhone XS'),
        ('iPhone XS Max', 'iPhone XS Max'),
        ('iPhone XR', 'iPhone XR'),
        ('iPhone 11', 'iPhone 11'),
        ('iPhone 11 Pro', 'iPhone 11 Pro'),
        ('iPhone 11 Pro Max', 'iPhone 11 Pro Max'),
        ('iPhone SE (2nd generation)', 'iPhone SE (2nd generation)'),
        ('iPhone 12 Mini', 'iPhone 12 Mini'),
        ('iPhone 12', 'iPhone 12'),
        ('iPhone 12 Pro', 'iPhone 12 Pro'),
        ('iPhone 12 Pro Max', 'iPhone 12 Pro Max'),
        ('iPhone 13 Mini', 'iPhone 13 Mini'),
        ('iPhone 13', 'iPhone 13'),
        ('iPhone 13 Pro', 'iPhone 13 Pro'),
        ('iPhone 13 Pro Max', 'iPhone 13 Pro Max'),
        ('Redmi Note 11', 'Redmi Note 11'),
        )
    modelo = models.CharField(max_length=50, choices=MODELO_TEL_OPT, null=False, blank=False)
    
    serial = models.CharField(max_length=30, null=False, blank=False, unique=True)
        
    tipo_almacenamiento = models.CharField(max_length=35, null=True, blank=True)
    
    almacenamiento = models.CharField(max_length=10, null=True, blank=True)
    
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
    sucursal = models.CharField(max_length=11, choices=SUCURSALES_OPT, null=False, blank=False, default="Chihuahua")
    
    asignado = models.BooleanField(default=False)
        
    def __str__(self):
        return f"{self.marca} {self.modelo}. Serial: {self.serial}"
    
class equipos_monitor(models.Model):
    MARCA_MON_OPT = (
        ('Dell', 'Dell'),
        ('Vorago', 'Vorago'),
        ('Samsung', 'Samsung'),
        ('LG', 'LG'),
        ('Alienware', 'Alienware'),
        ('AOC', 'AOC'),
        ('Asus', 'Asus'),
        ('Acer', 'Acer'),
        ('BenQ', 'BenQ'),
    )
    marca = models.CharField(max_length=10, default='Dell', choices=MARCA_MON_OPT, null=False, blank=False)
    
    modelo = models.CharField(max_length=50, null=False, blank=False)
    
    serial = models.CharField(max_length=100, null=False, blank=False, unique=True)
    
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
    sucursal = models.CharField(max_length=11, choices=SUCURSALES_OPT, null=False, blank=False, default="Chihuahua")
    
    asignado = models.BooleanField(default=False)
        
    def __str__(self):
        return f"{self.marca} {self.modelo}. Serial: {self.serial}"
    
class equipos_docking(models.Model):
    marca = models.CharField(max_length=25, null=False, blank=False)
    
    modelo = models.CharField(max_length=25, null=False, blank=False)
    
    serial = models.CharField(max_length=40, null=False, blank=False, unique=True)
    
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
    sucursal = models.CharField(max_length=11, choices=SUCURSALES_OPT, null=False, blank=False, default="Chihuahua")
    
    asignado = models.BooleanField(default=False)
        
    def __str__(self):
        return f"{self.marca} {self.modelo}. Serial: {self.serial}"
    
class equipos_tablet(models.Model):
    marca = models.CharField(max_length=25, null=False, blank=False)
    
    modelo = models.CharField(max_length=25, null=False, blank=False)
    
    serial = models.CharField(max_length=40, null=False, blank=False, unique=True)
    
    almacenamiento = models.CharField(max_length=10, null=True, blank=True)
    
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
    sucursal = models.CharField(max_length=11, choices=SUCURSALES_OPT, null=False, blank=False, default="Chihuahua")
    
    asignado = models.BooleanField(default=False)
        
    def __str__(self):
        return f"{self.marca} {self.modelo}. Serial: {self.serial}"
    
class equipos_mini_pc(models.Model):
    marca = models.CharField(max_length=25, null=False, blank=False)
    
    modelo = models.CharField(max_length=25, null=False, blank=False)
    
    serial = models.CharField(max_length=40, null=False, blank=False, unique=True)
    
    almacenamiento = models.CharField(max_length=10, null=True, blank=True)
    
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
    sucursal = models.CharField(max_length=11, choices=SUCURSALES_OPT, null=False, blank=False, default="Chihuahua")
    
    asignado = models.BooleanField(default=False)
        
    def __str__(self):
        return f"{self.marca} {self.modelo}. Serial: {self.serial}"
    
class equipos_handheld(models.Model):
    marca = models.CharField(max_length=10, null=False, blank=False, default="Zebra")
    MODELO_OPT = (
        ('TC26BK', 'TC26BK'),
        ('TC210K', 'TC210K'),
    )
    modelo = models.CharField(max_length=6, choices=MODELO_OPT, null=False, blank=False)
    serial = models.CharField(max_length=20, null=False, blank=False, unique=True)
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
    sucursal = models.CharField(max_length=11, choices=SUCURSALES_OPT, null=False, blank=False, default="Chihuahua")
    asignado = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.marca} {self.modelo}. Serial: {self.serial}"