from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import UrlForm
from .models import URL


class UrlShortenerView(View):

    def get(self, request):
        form = UrlForm()
        context = {
            'form': form,
            'title': 'OSAMA MOHAMED URL Shortener',
        }
        return render(request, 'shortener/url.html', context)

    def post(self, request):
        form = UrlForm(request.POST)
        context = {
            'form': form,
            'title': 'OSAMA MOHAMED URL Shortener',
        }
        template = 'shortener/url.html'
        if form.is_valid():
            new_url = form.cleaned_data.get('url')
            obj, created = URL.objects.get_or_create(url=new_url)
            context = {
                'object': obj,
            }
            if created:
                template = 'shortener/success.html'
            else:
                template = 'shortener/already_exists.html'

        return render(request, template, context)


class RedirectView(View):
    def get(self, request, short_url=None, *args, **kwargs):
        qs = URL.objects.filter(short_url__iexact=short_url)
        if qs.count() and qs.exists():
            obj = qs.first()
            return redirect(obj.url)
