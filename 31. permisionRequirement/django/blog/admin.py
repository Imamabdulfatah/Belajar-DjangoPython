from django.contrib import admin

# Register your models here.
from .models import Artikel

class ArtikelAdmin(admin.ModelAdmin):
   admin.site.register(Artikel)

# user dan password
# admin                    admin123
# ujang@gmail.com       UjangUjang
# otong@gmail.com          OtongOtong