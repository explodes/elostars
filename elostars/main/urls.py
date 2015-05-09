from django.conf.urls import patterns, url


urlpatterns = patterns("elostars.main.views",
    url("^(?P<version>v\d+)/events/$", "get_events", name="events"),
    url("^(?P<version>v\d+)/events/(?P<pk>\d+)/$", "get_event", name="event"),
    url("^(?P<version>v\d+)/events/(?P<slug>[A-Za-z0-9_-]+)/$", "get_event", name="event"),
)