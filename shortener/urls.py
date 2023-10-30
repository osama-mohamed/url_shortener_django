from django.urls import path

from .views import UrlShortenerView, RedirectView

app_name = 'shortener'

urlpatterns = [
  path(r'<path:short_url>/', RedirectView.as_view(), name='redirect'),
  path(r'', UrlShortenerView.as_view(), name='home'),
]