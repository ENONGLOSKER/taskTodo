# models.py
from django.db import models

class Task(models.Model):
    PRTY_CHOICES = [
        ('Prioritas', 'Prioritas'),
        ('Sedang', 'Sedang'),
        ('Santai', 'Santai')
    ]
    name = models.CharField(max_length=255)
    priority = models.CharField(max_length=255, choices=PRTY_CHOICES)
    tags = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ToDo(models.Model):
    STATUS_CHOICES = [
        ('todo', 'Akan Dikerjakan'),
        ('in_progress', 'Sedang Dikerjakan'),
        ('done', 'Sudah Dikerjakan'),
    ]

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='todos')
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')

    def __str__(self):
        return self.name
