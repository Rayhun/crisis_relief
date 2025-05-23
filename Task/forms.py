from django import forms
from .models import TaskComment, VolunteersRequest


class TaskCommentForms(forms.ModelForm):

    class Meta:
        model = TaskComment
        fields = ['comment', ]


class VolunteersRequestForm(forms.ModelForm):
    class Meta:
        model = VolunteersRequest
        fields = ['title', 'location', 'category', 'quantity', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'location': forms.TextInput(attrs={'placeholder': 'Enter location'}),
        }

    def __init__(self, *args, **kwargs):
        super(VolunteersRequestForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'placeholder': 'Enter title',
            'class': 'form-control'
        })
        self.fields['category'].widget.attrs.update({
            'class': 'form-select'
        })
        self.fields['quantity'].widget.attrs.update({
            'placeholder': 'Enter quantity',
            'class': 'form-control'
        })
