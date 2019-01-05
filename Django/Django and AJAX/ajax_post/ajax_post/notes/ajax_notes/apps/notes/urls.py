from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'all_note$', views.all_note),
    url(r'new_note$', views.new_note),
    url(r'(?P<note_id>\d+)/edit', views.edit),
    url(r'(?P<note_id>\d+)/delete$', views.delete),
]