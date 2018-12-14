from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^register$', views.index),
    url(r'^login$', views.login),
    url(r'^new$', views.new),
    url(r'^$', views.new_list)
]