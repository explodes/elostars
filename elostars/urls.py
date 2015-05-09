from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('elostars.main.urls', namespace="main")),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
