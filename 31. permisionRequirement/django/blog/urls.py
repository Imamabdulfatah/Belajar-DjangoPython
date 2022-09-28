from django.conf.urls import url

from .views import addView, indexView, updateView

urlpatterns = [
    url(r'update/$', updateView, name='update'),
    url(r'add/$', addView, name='add'),
    url(r'$', indexView, name='index'),

]