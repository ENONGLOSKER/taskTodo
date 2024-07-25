from django.contrib import admin
from .models import Task, ToDo
# Register your models here.
admin.site.register(ToDo)
admin.site.register(Task)