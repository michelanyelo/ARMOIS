# Generated by Django 5.0.1 on 2024-04-06 22:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armois', '0008_delete_horariodisponible'),
    ]

    operations = [
        migrations.AddField(
            model_name='horarioatencion',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
