from django import forms

from todo_list.models import ToDo, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    class Meta:
        model = ToDo
        fields = ("title", "tags")