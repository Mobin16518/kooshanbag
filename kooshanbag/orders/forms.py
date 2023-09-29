from django import forms



class AddresChose(forms.Form):
    addres = forms.CharField(widget=forms.RadioSelect())