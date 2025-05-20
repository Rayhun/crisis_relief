from django import forms
from .models import TaskComment


class TaskCommentForms(forms.ModelForm):

    class Meta:
        model = TaskComment
        fields = ['comment', ]
