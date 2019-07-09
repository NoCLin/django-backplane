from django.conf import settings
from django.urls import re_path, include

urlpatterns = []
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^silk/', include('silk.urls', namespace='silk'))
    ]
