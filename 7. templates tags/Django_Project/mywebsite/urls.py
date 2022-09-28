from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url yang kita buat
    url(r'^blog/', include('blog.urls')),
    url(r'^about/$', views.about),
    url(r'^$', views.index),
]
