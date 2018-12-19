from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.index, name="index"),
	url(r"^second$", views.level_two, name="second"),
	url(r"three$", views.level_three, name="three"),
	url(r"^make_data/", views.make_data, name="make_data"),
]