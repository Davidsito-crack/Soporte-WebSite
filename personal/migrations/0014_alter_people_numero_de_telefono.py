# Generated by Django 3.2.8 on 2024-08-02 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0013_alter_people_numero_de_empleado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='numero_de_telefono',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
