from django.core import validators
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django import forms
from .models import User

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["email", "f_name", "l_name", "phone"]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ["email", "phone", "password", "f_name", "l_name", "is_active", "is_admin"]



class LoginForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class' : 'inputs'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'inputs'}))
    



class RegisterForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'inputs'}), validators=[validators.EmailValidator])
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'inputs'}), validators=[validators.MaxLengthValidator(12)])
    fname = forms.CharField(widget=forms.TextInput(attrs={'class':'inputs'}))
    lname = forms.CharField(widget=forms.TextInput(attrs={'class':'inputs'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'inputs'}))
    password_conf = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'inputs'}))


class CheckOtpForm(forms.Form):
    otp_code = forms.CharField(widget=forms.TextInput(attrs={'class':'inputs'}))
    
    
    
class UserAddresForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'bill-input'}), validators=[validators.EmailValidator])
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'bill-input'}), validators=[validators.MaxLengthValidator(12)])
    f_name = forms.CharField(widget=forms.TextInput(attrs={'class':'bill-input'}))
    l_name = forms.CharField(widget=forms.TextInput(attrs={'class':'bill-input'}))
    plak = forms.CharField(widget=forms.TextInput(attrs={'class':'bill-input'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'bill-input'}))
    postal_code = forms.CharField(widget=forms.TextInput(attrs={'class':'bill-input'}))
    addres = forms.CharField(widget=forms.TextInput(attrs={'class':'bill-input'}))