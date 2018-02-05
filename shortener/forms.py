from django import forms
from .validators import validate_url, validate_domain


class UrlForm(forms.Form):
    url = forms.CharField(label='URL',
                          validators=[validate_url, validate_domain],
                          widget=forms.TextInput(
                              attrs={
                                  'class': 'form-control',
                                  'placeholder': 'Original URL Here'
                              }
                          ))
