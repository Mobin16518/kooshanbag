from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control text-center input-value'}))
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)
    color = forms.CharField()
