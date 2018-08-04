from django.conf.urls import url, include
from django.urls import re_path
from django.views.static import serve
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('app.app.urls')),
    url(r'^media/(?P<path>.*)',serve,{'document_root':settings.MEDIA_ROOT}),
]

