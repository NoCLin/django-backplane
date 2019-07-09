from django.conf import settings
from django.contrib import admin

admin.site.site_header = getattr(settings, 'SITE_HEADER', '')
admin.site.site_title = getattr(settings, 'SITE_FOOTER', '')
