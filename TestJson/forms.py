from django import forms
from .models import Email


class ContactForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['name', 'subject', 'e_mail', 'message']
        widgets = {
            'e_mail': forms.EmailInput(
                attrs={'id': 'email-id', 'required': True, 'placeholder': 'Your e-mail here'}
            ),
        }