# Generated by Django 5.0.3 on 2024-07-22 01:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('Prioritas', 'Prioritas'), ('Sedang', 'Sedang'), ('Santai', 'Santai')], default=True, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='tags',
            field=models.CharField(default=True, max_length=255),
            preserve_default=False,
        ),
    ]
