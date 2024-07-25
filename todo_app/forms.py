# forms.py
from django import forms
from .models import Task, ToDo

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'priority', 'tags']

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'style': 'width: 100%; padding: 12px 20px; border-radius: 6px; margin: 10px 0; background-color: #f8f8f838; border: none; font-size: 18px; color: white; text-transform: capitalize;',
                'placeholder': 'Tambahkan Todo'
            })
        }