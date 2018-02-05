from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


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
