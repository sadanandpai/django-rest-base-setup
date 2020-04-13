from django.urls import include, path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^(?P<path>.*)/$', views.index),
]