from django import forms

from todo_list.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    deadline = forms.DateTimeField(required=False)
    class Meta:
        model = Task
        fields = ("title", "deadline", "tags")