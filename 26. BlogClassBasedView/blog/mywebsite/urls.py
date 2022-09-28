from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^artikel/', include(('artikel.urls', 'artikel'), namespace='artikel')),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^admin/', admin.site.urls),
]
