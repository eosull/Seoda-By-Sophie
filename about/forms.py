# Create django forms for FAQs and contact

from django import forms
from django.core.validators import EmailValidator

from .models import Faq
from products.models import Product


class ContactForm(forms.Form):
    # Declaring fields for contact form
    name = forms.CharField(max_length=100, required=True)
    email = forms.CharField(validators=[EmailValidator()], required=True)
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
        # Add placeholders
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'email': 'Email Address',
            'subject': 'Subject',
            'message': 'Message',
        }

        # Add custom styling including autofocus on name, * symbol on required
        # fields and assigning placeholders and style classes
        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input \
                 py-2 my-3'
            self.fields[field].label = False


class FaqForm(forms.ModelForm):
    # Inheriting Faq model for fields
    class Meta:
        model = Faq
        fields = '__all__'

    # Set stying for form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'stripe-style-input my-3'
