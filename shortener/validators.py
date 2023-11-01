from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.conf import settings


def validate_url(value):
  url_validator = URLValidator()
  reg_value = value
  if 'https://' in reg_value:
    new_value = reg_value
  elif 'http://' in reg_value:
    new_value = reg_value
  else:
    new_value = 'https://' + value
  try:
    url_validator(new_value)
  except:
    raise ValidationError('invalid URL syntax')
  return new_value


def validate_domain(value):
  if '.' not in value:
    raise ValidationError('invalid URL syntax because no . in url')
  return value


def validate_short_url(value):
  if len(value) < settings.SHORTCODE_MIN:
    raise ValidationError(f'invalid Coustom URL length, must be more than or equal to: {settings.SHORTCODE_MIN}')
  if len(value) > settings.SHORTCODE_MAX:
    raise ValidationError(f'invalid Coustom URL length, must be less than or equal to: {settings.SHORTCODE_MAX}')
  return value