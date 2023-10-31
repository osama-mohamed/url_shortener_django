from django.contrib import admin

from .models import URL, Analytics


class UrlModelAdmin(admin.ModelAdmin):
  list_display = [
    'id',
    'active',
    'qr_code',
    'url',
    'short_url',
    'clicks',
    'added',
  ]
  list_display_links = ['id']
  list_editable = ['active', 'url', 'short_url', 'clicks']
  list_filter = [
    'clicks',
    'active',
    'added',
  ]
  search_fields = ['url', 'short_url', 'clicks']
  list_per_page = 50

  class Meta:
    model = URL


class AnalyticsModelAdmin(admin.ModelAdmin):
  list_display = [
    'short_url',
    'get_short_url',
    'ip_address',
    'timestamp',
  ]
  list_per_page = 50
  
  class Meta:
    model = Analytics

  def get_short_url(self, obj):
    return obj.short_url.short_url


admin.site.register(URL, UrlModelAdmin)
admin.site.register(Analytics, AnalyticsModelAdmin)