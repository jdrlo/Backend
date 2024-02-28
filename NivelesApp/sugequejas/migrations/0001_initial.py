# Generated by Django 4.2.7 on 2023-11-22 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SugeQuejas',
            fields=[
                ('id_SugeQuejas', models.AutoField(primary_key=True, serialize=False)),
                ('suge_Queja', models.TextField(max_length=1000)),
                ('estado', models.CharField(choices=[('Sugerencia', 'Sugerencia'), ('Quejas', 'Quejas')], verbose_name='Estado')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Sugerencia/Queja')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
