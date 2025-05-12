from django import forms
from Affected.models import ReliefRequest


class RequestForm(forms.ModelForm):
    class Meta:
        model = ReliefRequest
        fields = ['title', 'description', 'category', 'location', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }
