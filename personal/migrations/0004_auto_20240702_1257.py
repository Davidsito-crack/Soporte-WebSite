# Generated by Django 3.2.8 on 2024-07-02 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_rename_n_phone_people_numero_de_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='VPN',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='people',
            name='contrasena_VPN',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='people',
            name='contrasena_correo',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='people',
            name='correo',
            field=models.CharField(blank=True, default='@mscdirect.com.mx', max_length=100, null=True),
        ),
    ]
