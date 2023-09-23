from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your name")
    phone = forms.CharField(max_length=100, label="Your phone")
    content = forms.CharField(max_length=100, label="Your Details")
