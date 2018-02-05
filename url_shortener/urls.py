from django.conf.urls import url
from django.contrib import admin

from shortener.views import UrlShortenerView, RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<short_url>[\w-]+)/$', RedirectView.as_view(), name='redirect'),
    url(r'^$', UrlShortenerView.as_view(), name='home'),
]
