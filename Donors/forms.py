from django import forms
from .models import Donation


class GoodsDonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = [
            'item_name',
            'contact_info',
            'delivery_time',
            'item_description',
            'pickup_address',
        ]

        widgets = {
            'item_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter the name of the item',
                    'required': 'required',
                }
            ),
            'contact_info': forms.TextInput(
                attrs={
                    'placeholder': 'Enter the contract information'
                }
            ),
            'delivery_time': forms.DateInput(attrs={'type': 'date'}),
            'item_description': forms.Textarea(),
            'pickup_address': forms.TextInput(
                attrs={'placeholder': 'Enter the pickup address'}
            ),
        }
        help_texts = {
            'item_description': '''
            Please provide details like.
            <small>
            <ul>
                <li>For food: names, types (dry/cooked), quantity (e.g. 5kg rice, 10 packets of biscuits)</li>
                <li>For medicine: names, expiry date, quantity (e.g. 10 strips of Paracetamol).</li>
                <li>For other goods: item type, condition, quantity (e.g. 3 wool blankets, used but clean)</li>
            </ul>
            </small>
            '''
        }
