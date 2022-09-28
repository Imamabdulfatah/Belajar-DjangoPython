from django.conf.urls import url
#from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    url(r'^$', views.index),
]