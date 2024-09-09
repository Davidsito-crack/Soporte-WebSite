# Generated by Django 3.2.8 on 2024-08-09 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0013_equipos_handheld_sucursal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipos_laptop',
            name='modelo',
            field=models.CharField(choices=[('Latitude 3510', 'Latitude 3510'), ('Latitude 3520', 'Latitude 3520'), ('Latitude 3540', 'Latitude 3540'), ('Latitude 3550', 'Latitude 3550'), ('Inspiron 3583', 'Inspiron 3583'), ('Inspiron 5540', 'Inspiron 5520'), ('Inspiron 5530', 'Inspiron 5530'), ('Inspiron 5540', 'Inspiron 5540'), ('Inspiron 5570', 'Inspiron 5570'), ('Precision 7780', 'Precision 7780'), ('XPS 13 9350', 'XPS 13 9350'), ('XPS 13 9360', 'XPS 13 9360'), ('XPS 13 9370', 'XPS 13 9370'), ('XPS 13 9380', 'XPS 13 9380')], max_length=15),
        ),
        migrations.AlterField(
            model_name='equipos_telefono',
            name='marca',
            field=models.CharField(choices=[('Samsung', 'Samsung'), ('Apple', 'Apple'), ('Xiaomi', 'Xiaomi'), ('TCL', 'TCL')], max_length=7),
        ),
        migrations.AlterField(
            model_name='equipos_telefono',
            name='modelo',
            field=models.CharField(choices=[('T770B', 'T770B'), ('Galaxy A03s', 'Galaxy A03s'), ('Galaxy A20s', 'Galaxy A20s'), ('Galaxy A33 5G', 'Galaxy A33 5G'), ('Galaxy A50', 'Galaxy A50'), ('Galaxy A51', 'Galaxy A51'), ('Galaxy S23 Ultra', 'Galaxy S23 Ultra'), ('Galaxy S23 Plus', 'Galaxy S23 Plus'), ('Galaxy S23', 'Galaxy S23'), ('Galaxy S24 Ultra', 'Galaxy S24 Ultra'), ('Galaxy S24 Plus', 'Galaxy S24 Plus'), ('Galaxy S24', 'Galaxy S24'), ('iPhone X', 'iPhone X'), ('iPhone XS', 'iPhone XS'), ('iPhone XS Max', 'iPhone XS Max'), ('iPhone XR', 'iPhone XR'), ('iPhone 11', 'iPhone 11'), ('iPhone 11 Pro', 'iPhone 11 Pro'), ('iPhone 11 Pro Max', 'iPhone 11 Pro Max'), ('iPhone SE (2nd generation)', 'iPhone SE (2nd generation)'), ('iPhone 12 Mini', 'iPhone 12 Mini'), ('iPhone 12', 'iPhone 12'), ('iPhone 12 Pro', 'iPhone 12 Pro'), ('iPhone 12 Pro Max', 'iPhone 12 Pro Max'), ('iPhone 13 Mini', 'iPhone 13 Mini'), ('iPhone 13', 'iPhone 13'), ('iPhone 13 Pro', 'iPhone 13 Pro'), ('iPhone 13 Pro Max', 'iPhone 13 Pro Max'), ('Redmi Note 11', 'Redmi Note 11')], max_length=50),
        ),
    ]
