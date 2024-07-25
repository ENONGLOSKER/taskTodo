# Generated by Django 5.0.3 on 2024-07-21 22:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('todo', 'Akan Dikerjakan'), ('in_progress', 'Sedang Dikerjakan'), ('done', 'Sudah Dikerjakan')], default='todo', max_length=20)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todos', to='todo_app.task')),
            ],
        ),
    ]