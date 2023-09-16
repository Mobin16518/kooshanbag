from django.forms import ModelForm
from .models import UserContact



class UserContactForm(ModelForm):
    class Meta:
        model = UserContact
        fields = ['name', 'phone', 'email', 'title', 'text']