# Generated by Django 3.2.8 on 2024-08-02 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0011_alter_comodatos_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='contrasena_VPN',
        ),
        migrations.RemoveField(
            model_name='people',
            name='contrasena_correo',
        ),
        migrations.AddField(
            model_name='people',
            name='numero_de_empleado',
            field=models.CharField(default='...', max_length=4),
        ),
    ]
