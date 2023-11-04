from django import forms
from .validators import validate_url, validate_short_url
from django.core.validators import RegexValidator

from django.utils.safestring import mark_safe

from .models import URL


class UrlForm(forms.Form):
  url = forms.CharField(
    label='URL',
    validators=[validate_url,],
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'placeholder': 'Original URL Here'
      }
    )
  )

  short_url = forms.CharField(
    label='Custom URL',
    validators=[
      validate_short_url,
      RegexValidator(
        regex=r'^[a-zA-Z0-9]+$',
        message=f'invalid Coustom URL regular expressions, Should contain (A-Z a-z 0-9) only.',
      ),
      ],
    required=False,
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'placeholder': 'Custom URL Here'
      }
    ),
  )

  def clean_short_url(self):
    short_url = self.cleaned_data.get('short_url')
    if short_url:
      qs = URL.objects.filter(short_url__exact=short_url)
      if qs.exists():
        raise forms.ValidationError(mark_safe(f'Sorry the Custom URL already exists, Choose another OR <a href="{qs.first().get_short_url()}" target="_blank">Redirect</a> to it.'))
    return short_url