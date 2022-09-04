from dataclasses import fields
from .models import Task
from django.forms import ModelForm, widgets, TextInput, Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task', 'exec_time']
        widgets = {'title':TextInput(attrs={'class':'form-control', 'placeholder':'Введите название'}),
                   'task':Textarea(attrs={'class':'form-control', 'placeholder':'Введите описание'}),
                   'exec_time':TextInput(attrs = {'class':'form-control', 'placeholder':'Укажите время выполнения'})}


