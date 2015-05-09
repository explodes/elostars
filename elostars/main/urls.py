from django.conf.urls import patterns, url

urlpatterns = patterns("elostars.main.views",
    url("^$", "home", name="home"),
    url("^signup/$", "signup", name="signup"),
    url("^settings/$", "user_settings", name="settings"),
    url("^rate/$", "rate", name="rate"),
)