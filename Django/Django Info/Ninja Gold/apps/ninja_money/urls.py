from django.conf.urls import url
from . import views

urlpatterns = [ #all the urls that are valid for this app
    url(r'^$', views.index), # ^ = the beginning of and $ = the end of the url page
    url(r'^login$', views.login),
    url(r'process/(?P<location>\w+)$', views.process)
]
