# Generated by Django 4.2.6 on 2023-10-12 21:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventos',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]