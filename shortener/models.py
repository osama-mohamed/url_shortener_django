from django.db import models
from django.conf import settings

from .utils import create_shortcode

SHORTCODE_MAX = getattr(settings, 'SHORTCODE_MAX', 15)


class URL(models.Model):
    url = models.CharField(max_length=250)#, validators=[validate_url, validate_domain])
    short_url = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    clicks = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.url)

    def save(self, *args, **kwargs):
        if self.short_url is None or self.short_url == '':
            self.short_url = create_shortcode(self)
        if not 'http' in self.url:
            self.url = 'http://' + self.url
        super(URL, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return 'http://localhost:8000/{shortcode}'.format(shortcode=self.short_url)

    def get_short_url(self):
        # url_path = reverse('scode', kwargs={'shortcode': self.shortcode})
        # return 'http://localhost:8000' + url_pat
        return 'http://localhost:8000/{shortcode}'.format(shortcode=self.short_url)
