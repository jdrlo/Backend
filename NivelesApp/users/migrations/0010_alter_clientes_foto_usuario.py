# Generated by Django 4.2.6 on 2024-03-06 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_clientes_foto_clientes_foto_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='foto_Usuario',
            field=models.ImageField(blank=True, null=True, upload_to='foto_Usuario/%Y%m/', verbose_name='Foto Usuario'),
        ),
    ]
