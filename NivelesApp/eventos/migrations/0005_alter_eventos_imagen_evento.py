# Generated by Django 4.2.6 on 2024-03-01 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0004_rename_foto_eventos_imagen_evento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='imagen_Evento',
            field=models.ImageField(blank=True, null=True, upload_to='eventos/%Y%m/', verbose_name='Foto'),
        ),
    ]