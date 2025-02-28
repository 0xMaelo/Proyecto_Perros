# Generated by Django 5.1.6 on 2025-02-24 21:48

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perros', '0003_remove_perro_edad_remove_perro_perdido_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='perro',
            name='collar',
            field=models.CharField(choices=[('si', 'Sí'), ('no', 'No')], default='Sin collar', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perro',
            name='color_collar',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='perro',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='perros_fotos/'),
        ),
        migrations.AddField(
            model_name='perro',
            name='raza',
            field=models.CharField(default='mestizo', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perro',
            name='sexo',
            field=models.CharField(choices=[('macho', 'Macho'), ('hembra', 'Hembra')], default='macho', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perro',
            name='tamano',
            field=models.CharField(choices=[('pequeno', 'Pequeño'), ('mediano', 'Mediano'), ('grande', 'Grande')], default='grande', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='perro',
            name='fecha_perdido',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='perro',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
