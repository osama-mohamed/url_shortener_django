from django.contrib import admin

from .models import URL


class UrlModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'url',
        'short_url',
        'clicks',
        'added',
    ]
    list_display_links = ['id']
    list_editable = ['url', 'short_url', 'clicks']
    list_filter = [
        'clicks',
        'active',
        'added',
    ]
    search_fields = ['url', 'short_url', 'clicks']
    list_per_page = 50

    class Meta:
        model = URL


admin.site.register(URL, UrlModelAdmin)
