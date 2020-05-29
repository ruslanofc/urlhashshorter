from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.sites.shortcuts import get_current_site
from django.utils.safestring import mark_safe

from core.models import URL


if admin.site.is_registered(Group):
    admin.site.unregister(Group)


class URLAdmin(admin.ModelAdmin):
    list_display = ('source_url', 'get_short_slug', 'views')
    fieldsets = (
        (None, {
            'fields': ('source_url',),
        }),
    )
    ordering = ('-views',)

    def get_queryset(self, request):
        current_site = get_current_site(request)
        self.domain = current_site.domain
        return super(URLAdmin, self).get_queryset(request)

    def get_short_slug(self, obj):
        url = 'http://{}{}'.format(self.domain, obj.get_absolute_url())
        return mark_safe('<a href="{}">{}</a>'.format(url, url))


admin.site.register(URL, URLAdmin)
