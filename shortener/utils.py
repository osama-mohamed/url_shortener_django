import random
import string
from django.conf import settings


SHORTCODE_MIN = getattr(settings, 'SHORTCODE_MIN', 6)


def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits + string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance, size=SHORTCODE_MIN):
    new_code = code_generator(size=size)
    klass = instance.__class__
    qs_exists = klass.objects.filter(short_url=new_code).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new_code
