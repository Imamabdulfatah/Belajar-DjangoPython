from django.conf.urls import url

from .views import artikelIndexView, artikelAddView, artikelAddView2, otongView

urlpatterns = [
    url('^otong/$', otongView, name='otong'),
    url('^add2/$', artikelAddView2, name='add2'),
    url('^add/$', artikelAddView, name='add' ),
    url(r'^$', artikelIndexView, name="index"),
]