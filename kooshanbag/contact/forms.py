from django import forms
from django.core import validators



class UserContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'inputs', 'id':'name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'inputs', 'id':'email'}), validators=[validators.EmailValidator])
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'inputs', 'id':'phn'}), validators=[validators.MaxLengthValidator(12)])
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'inputs', 'id':'sub'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class':'inputs', 'id':'msg'}))