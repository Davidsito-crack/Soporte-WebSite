# Generated by Django 3.2.8 on 2024-07-08 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0005_people_sucursal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='sucursal',
            field=models.CharField(choices=[('Chihuahua', 'Chihuahua'), ('Juárez', 'Juárez'), ('Guaymas', 'Guaymas'), ('Monterrey', 'Monterrey'), ('Tamaulipas', 'Tamaulipas'), ('Querétaro', 'Querétaro'), ('Mexicali', 'Mexicali'), ('Silao', 'Silao'), ('Guanajuato', 'Guanajuato'), ('CDMX', 'CDMX'), ('Tijuana', 'Tijuana'), ('Guadalajara', 'Guadalajara')], default='...', max_length=25),
        ),
    ]
