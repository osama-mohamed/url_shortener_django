import random, os, string, qrcode
from django.conf import settings
from django.core.files import File

from io import BytesIO

SHORTCODE_MIN = getattr(settings, 'SHORTCODE_MIN', 6)


def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits + string.ascii_uppercase):
  return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance, size=SHORTCODE_MIN):
  new_code = code_generator(size=size)
  klass = instance.__class__
  qs = klass.objects.filter(short_url=new_code)
  if qs.exists():
    return create_shortcode(instance, size=size)
  return new_code


def check_qr_img(instance, request=None):
  if instance.short_url:
    file_path = os.path.join(settings.MEDIA_ROOT, settings.SHORTENER_QR_CODE_DIR, f'{instance.short_url}.png')
    if not os.path.isfile(file_path):
      generate_and_save_qr_code(instance, request=request)


def generate_and_save_qr_code(instance, request=None):
  qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
  )
  data = settings.URL + '/' + instance.short_url + '/'
  qr.add_data(data)
  qr.make(fit=True)
  img = qr.make_image(fill_color='black', back_color='white')
  buffer = BytesIO()
  img.save(buffer, 'PNG')
  name = f'{instance.short_url}.png'
  image_file = File(buffer, name=name)
  instance.qr_code.save(name, image_file)
  instance.save()
  return instance.qr_code.url