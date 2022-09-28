from django.contrib import admin

# Register your models here.
from .models import Artikel

class ArtikelAdmin(admin.ModelAdmin):
   
    def get_readonly_fields(self, request, obj):

        current_user = request.user
        # ini untuk editor
        if obj != None:
            if current_user.hash_perm("blog.published_artikel"):
                readonly_fields = [
                                'created',
                                'updated',
                                'published',
                                'slug',
                            ]
                return readonly_fields
            # ini adalah penulis
            elif current_user.hash_perm("blog.add_artikel"):

                if obj.is_published:
                    return [data.name for data in self.model._meta.fields]
                else:
                    readonly_fields = [
                                    'created',
                                    'updated',
                                    'is_published',
                                    'published',
                                    'slug',
                                ]
                    return readonly_fields
        else:
            readonly_fields = [
                                'created',
                                'updated',
                                'is_published',
                                'published',
                                'slug',
                            ]
            return readonly_fields

admin.site.register(Artikel, ArtikelAdmin)

# user dan password
# admin                    admin123
# ujang@gmail.com       UjangUjang
# otong@gmail.com          OtongOtong