# Generated by Django 4.2.6 on 2024-03-08 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_clientes_foto_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientes',
            name='foto_Usuario',
        ),
        migrations.AddField(
            model_name='clientes',
            name='imagen_Usuario',
            field=models.ImageField(blank=True, null=True, upload_to='perfil/%Y%m/', verbose_name='Imagen Usuario'),
        ),
    ]
