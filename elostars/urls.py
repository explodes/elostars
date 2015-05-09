from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('elostars.main.urls', namespace="main")),

    url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
