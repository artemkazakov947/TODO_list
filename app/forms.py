from django import forms

from app.models import Tag, Task


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    deadline = forms.DateTimeField(widget=forms.SelectDateWidget)

    class Meta:
        model = Task
        fields = "__all__"
