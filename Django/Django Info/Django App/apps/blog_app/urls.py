from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), #@app.route('/')
    url(r'new$', views.new), #no need for a / because it will automatically put one in for you
    url(r'create$', views.create),
    url(r'show/(?P<number>\d+)$', views.show),
    url(r'^edit/(?P<word>\w+)$', views.edit),
    url(r'destroy$', views.destroy),
]

