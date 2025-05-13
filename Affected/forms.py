from django import forms
from Affected.models import ReliefRequest, Event


class RequestForm(forms.ModelForm):
    class Meta:
        model = ReliefRequest
        fields = [
            'event', 'title', 'description', 'category', 'location',
            'quantity', 'status'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date', 'latitude', 'longitude', 'location',
                  'radius', 'affected_people', 'status', 'description']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'datetime-local',
                }
            ),
            'latitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'radius': forms.NumberInput(attrs={'class': 'form-control'}),
            'affected_people': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Event Title',
            'date': 'Event Date',
            'latitude': 'Latitude',
            'longitude': 'Longitude',
            'location': 'Location',
            'radius': 'Radius (in km)',
            'affected_people': 'Affected People Count',
            'status': 'Status',
            'description': 'Description',
        }
