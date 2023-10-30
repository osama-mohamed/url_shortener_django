from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import Http404

from pprint import pprint

from .forms import UrlForm
from .models import URL, Analytics
from .utils import check_qr_img
from .analytics_utils import get_client_ip, get_country, get_platform_browser


class UrlShortenerView(View):
  def get(self, request):
    # print(request.build_absolute_uri())
    # scheme = request.scheme  # 'http' or 'https'
    # host = request.get_host()  # 127.0.0.1:8000 Hostname and the port
    # path = request.path  # / URL path without domain
    # print(f'{scheme}://{host}{path}')
    form = UrlForm(None)
    context = {
      'form': form,
      'title': 'OSAMA MOHAMED URL Shortener',
    }
    return render(request, 'shortener/url.html', context)

  def post(self, request):
    form = UrlForm(request.POST, None)
    context = {
      'form': form,
      'title': 'OSAMA MOHAMED URL Shortener',
    }
    template = 'shortener/url.html'
    if form.is_valid():
      url = form.cleaned_data.get('url')
      if 'https://' not in url and 'http://' not in url:
        new_url = 'https://' + url
      else:
        new_url = url
      obj, created = URL.objects.get_or_create(url=new_url)
      check_qr_img(obj, request)
      context = {
        'object': obj,
      }
      if created:
        template = 'shortener/success.html'
      else:
        template = 'shortener/already_exists.html'
    return render(request, template, context)

class RedirectView(View):
  def get(self, request, short_url=None):
    ip = get_client_ip(request)
    data = get_country(ip)
    parsed_data = get_platform_browser(request.META.get('HTTP_USER_AGENT', ''))

    country_code = data.get('country_code')
    country_name = data.get('country_name')
    region_name = data.get('region_name')
    city_name = data.get('city_name')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    zip_code = data.get('zip_code')
    time_zone = data.get('time_zone')
    net_provider = data.get('as')
    net_provider_code = data.get('asn')

    platform_name = parsed_data.get('platform').get('name')
    platform_version = parsed_data.get('platform').get('version')
    os_name = parsed_data.get('os').get('name')
    os_version = parsed_data.get('os').get('version')
    browser_name = parsed_data.get('browser').get('name')
    browser_version = parsed_data.get('browser').get('version')



    # for header, value in request.META.items():
    #   if header.startswith('HTTP_'):
    #     print(f"{header}: {value}")


    qs = URL.objects.filter(short_url__iexact=short_url, active=True)
    if qs.exists() and qs.count() == 1:
      obj = qs.first()
      obj.clicks += 1
      obj.save()
      a_obj = Analytics.objects.create(
        short_url=obj,
        ip_address=ip,
        country=country_name,
        country_code=country_code,
        region_name=region_name,
        city_name=city_name,
        latitude=latitude,
        longitude=longitude,
        zip_code=zip_code,
        time_zone=time_zone,
        net_provider=net_provider,
        net_provider_code=net_provider_code,
        platform=platform_name,
        platform_version=platform_version,
        os=os_name,
        os_version=os_version,
        browser=browser_name,
        browser_version=browser_version,
      )
      a_obj.clicks += 1
      a_obj.save()
      return redirect(obj.url)
    else:
      raise Http404