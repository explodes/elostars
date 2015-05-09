from django.conf.urls import patterns, url


urlpatterns = patterns("elostars.main.views",
    url("^$", "home", name="home"),
)