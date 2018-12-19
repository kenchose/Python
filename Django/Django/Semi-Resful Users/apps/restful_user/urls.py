from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^add$', views.add),
    url(r'(?P<user_id>\d+)$', views.show), #parameter to grab the user_id so we can upload our show page
    url(r'(?P<user_id>\d+)/edit$', views.edit),
    url(r'(?P<user_id>\d+)/destroy$', views.delete)

]