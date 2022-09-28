from django.conf.urls import url

from . import views

urlPatterns = [
    url(r'^$',views.index),
    url(r'^(?P<categoryInput>[\w-]+)/$',views.categoryPost),
    url(r'^post/(?P<slugInput>[\w-]+)/$',views.singlePost),
]