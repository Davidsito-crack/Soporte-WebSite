# Generated by Django 3.2.8 on 2024-06-28 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_people_n_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='n_phone',
            new_name='numero_de_telefono',
        ),
    ]
