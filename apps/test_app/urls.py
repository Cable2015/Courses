from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses$', views.courses),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^confirm/(?P<id>\d+)$', views.confirm),
    url(r'^NO$', views.NO),


]
