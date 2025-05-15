from django import forms
from .models import Donation


class GoodsDonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = [
            'pickup_latitude',
            'pickup_longitude',
            'quantity',
            'pickup_address',
            'delivery_time',
            'item_description',
        ]
