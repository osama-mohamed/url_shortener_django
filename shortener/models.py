from django.db import models
from django.conf import settings
from django.urls import reverse

SHORTCODE_MAX = getattr(settings, 'SHORTCODE_MAX', 15)


class URL(models.Model):
  url = models.CharField(max_length=250)
  short_url = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
  clicks = models.PositiveIntegerField(default=0)
  active = models.BooleanField(default=True)
  qr_code = models.ImageField(upload_to=settings.SHORTENER_QR_CODE_DIR, blank=True, null=True)
  added = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return str(self.url)

  def get_short_url(self):
    return reverse('shortener:redirect', kwargs={'short_url': self.short_url})
  

class Analytics(models.Model):
  short_url = models.ForeignKey(URL, on_delete=models.CASCADE)
  country = models.CharField(max_length=250, blank=True, null=True)
  country_code = models.CharField(max_length=250, blank=True, null=True)
  region_name = models.CharField(max_length=250, blank=True, null=True)
  city_name = models.CharField(max_length=250, blank=True, null=True)
  latitude = models.CharField(max_length=250, blank=True, null=True)
  longitude = models.CharField(max_length=250, blank=True, null=True)
  ip_address = models.CharField(max_length=250, blank=True, null=True)
  net_provider = models.CharField(max_length=250, blank=True, null=True)
  net_provider_code = models.CharField(max_length=250, blank=True, null=True)
  zip_code = models.CharField(max_length=250, blank=True, null=True)
  time_zone = models.CharField(max_length=250, blank=True, null=True)
  browser = models.CharField(max_length=250, blank=True, null=True)
  browser_version = models.CharField(max_length=250, blank=True, null=True)
  platform = models.CharField(max_length=250, blank=True, null=True)
  platform_version = models.CharField(max_length=250, blank=True, null=True)
  os = models.CharField(max_length=250, blank=True, null=True)
  os_version = models.CharField(max_length=250, blank=True, null=True)
  timestamp = models.DateTimeField(auto_now_add=True)


  def __str__(self):
    return str(self.short_url)