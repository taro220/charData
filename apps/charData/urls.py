from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^getCharData$', views.char_json)
]
