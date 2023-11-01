from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.conf import settings

import re


def validate_url(value):
  url_regex = re.compile(
    r'^(?:(?P<scheme>[a-zA-Z]+)://)?'  # Optional scheme (letters only) followed by '://'
    r'(?P<host>[a-z0-9.-]+)?'          # Optional host (letters, digits, dots, and hyphens)
    r'(?::(?P<port>\d+))?'             # Optional port (digits after colon)
    r'(?P<path>/.*)?$',                # Optional path (starting with '/')
    re.IGNORECASE
  )
  match = url_regex.match(value)
  if not match:
    raise ValidationError('invalid URL syntax')
  url_validator = URLValidator()
  try:
    url_validator(value)
  except ValidationError:
    raise ValidationError('Invalid URL syntax validation, URL must start with "http://" or "https://", and have a valid domain name (e.g. google.com)')
  return value


def validate_short_url(value):
  if len(value) < settings.SHORTCODE_MIN:
    raise ValidationError(f'invalid Coustom URL length, must be more than or equal to: {settings.SHORTCODE_MIN}')
  if len(value) > settings.SHORTCODE_MAX:
    raise ValidationError(f'invalid Coustom URL length, must be less than or equal to: {settings.SHORTCODE_MAX}')
  return value