from django.conf.urls import url, include
from django.contrib import admin
urlpatterns = [
    url(r'^users/', include ('apps.restful_user.urls')),
]
