from django.forms import ModelForm
from django import forms

from app.models import Task, Tag


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ("content", "deadline", "tags")
        widgets = {
            "deadline": forms.DateInput(attrs={"type": "datetime-local"})
        }


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
