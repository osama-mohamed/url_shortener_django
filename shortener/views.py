from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import Http404

from .forms import UrlForm
from .models import URL
from .utils import create_shortcode, check_qr_img
from .analytics_utils import return_analytics_data
from .analytics_create import create_new_analytics


class UrlShortenerView(View):
  def get(self, request):
    form = UrlForm(None)
    context = {'form': form, 'title': 'OSAMA MOHAMED URL Shortener'}
    return render(request, 'shortener/url.html', context)

  def post(self, request):
    form = UrlForm(request.POST, None)
    context = {'form': form, 'title': 'OSAMA MOHAMED URL Shortener'}
    template = 'shortener/url.html'
    if form.is_valid():
      url = form.cleaned_data.get('url')
      short_url = form.cleaned_data.get('short_url')
      obj, created = URL.objects.get_or_create(url=url)
      if created:
        obj.short_url = short_url if short_url else create_shortcode(obj)
        obj.save()
      check_qr_img(obj, request)
      context['object'] = obj
      template = 'shortener/success.html' if created else 'shortener/already_exists.html'
    return render(request, template, context)


class RedirectView(View):
  def get(self, request, short_url=None):
    ip, data, parsed_data = return_analytics_data(request)
    qs = URL.objects.filter(short_url__exact=short_url, active=True)
    if qs.exists() and qs.count() == 1:
      obj = qs.first()
      obj.clicks += 1
      obj.save()
      create_new_analytics(ip, data, parsed_data, obj)
      return redirect(obj.url)
    else:
      raise Http404