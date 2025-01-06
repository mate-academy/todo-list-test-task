from django import forms
from .models import Task, Tag

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['content', 'deadline', 'tags', 'is_done']
        widgets = {
            'tags': forms.TextInput(attrs={'placeholder': 'Enter tags separated by commas'}),
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
