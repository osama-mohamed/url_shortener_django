from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

from .utils import create_shortcode

SHORTCODE_MAX = getattr(settings, 'SHORTCODE_MAX', 15)


class URL(models.Model):
    url = models.CharField(max_length=250)
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
        super(URL, self).save(*args, **kwargs)

    def get_short_url(self):
        return 'http://localhost:8000' + reverse('redirect', kwargs={'short_url': self.short_url})
