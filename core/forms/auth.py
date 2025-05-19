from django import forms
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.layout import Layout, Submit, Row, Column, Field
from core.models import User
from core.models.user import USER_TYPE_CHOICES


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'login-form'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Field('username', css_class='form-control-lg'),
            Field('password', css_class='form-control-lg'),
            Submit('submit', 'Login', css_class='btn-primary btn-lg')
        )


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username', 'email', 'user_type', 'first_name', 'last_name',
            'address', 'password1', 'password2'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column('user_type', css_class='form-control col-md-6 mb-0'),
            ),
            Row(
                Column('password1', css_class='form-group col-md-6 mb-0'),
                Column('password2', css_class='form-group col-md-6 mb-0'),
            ),
            Submit('submit', 'Sign Up', css_class='btn-primary btn-block')
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.user_type = self.cleaned_data['user_type']
        if commit:
            user.save()
        return user


class ProfileForms(forms.ModelForm):
    class Meta():
        model = User
        fields = (
            'first_name', 'last_name', 'address', 'phone_number',
            'profile_picture', 'skill'
        )
