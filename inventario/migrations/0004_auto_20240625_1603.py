# Generated by Django 3.2.8 on 2024-06-25 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_alter_equipos_monitor_marca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipos_docking',
            name='serial',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='equipos_laptop',
            name='serial',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='equipos_mini_pc',
            name='serial',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='equipos_monitor',
            name='serial',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='equipos_tablet',
            name='serial',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='equipos_telefono',
            name='serial',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
