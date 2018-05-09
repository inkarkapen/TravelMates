from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add', views.add),
    url(r'^create', views.create),
    url(r'^join/(?P<id>\d+)$', views.join),
    url(r'^destination/(?P<id>\d+)$', views.show),
    url(r'^logout', views.logout)
]