# Generated by Django 4.2.6 on 2024-02-28 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_eventos_created_eventos_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='publicidad/%Y%m/', verbose_name='Foto'),
        ),
    ]
