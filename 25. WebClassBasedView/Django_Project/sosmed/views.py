from typing import ContextManager, Pattern
from django.shortcuts import render, redirect
from django.views.generic.base import RedirectView, TemplateView, View

# Create your views here.

from .models import Instagram
from .forms import InstagramForm

# membuat mixin  
class SosmedSubList:

    def get_list_data(self, get_request):
        if len(get_request) == 0:
            sublist = Instagram.objects.all()
        elif get_request.__contains__('content_filter'):
            sublist = Instagram.objects.filter(content = get_request['content_filter'])
        else:
            sublist = Instagram.objects.none()
        return sublist

        sublist = Instagram.objects.filter(content = content_filter)
        return sublist

# belajar di mro di kelas terbuka
class SosmedListView(SosmedSubList, TemplateView):
    template_name = 'sosmed/list.html'

    def get_context_data(self, *args, **kwargs):
        # semua_akun = Instagram.objects.all()
        list_akun = self.get_list_data(self.request.GET)
        list_content = Instagram.objects.values_list('content', flat=True).distinct()
        print(list_content)
        context = {
            'page_title':'sosial media memakai class baseview',
            'semua_akun':list_akun,
            'list_content':list_content,
        }
        return context


class SosmedDeleteView(RedirectView):
    pattern_name = 'sosmed:list'

    def get_redirect_url(self, *args, **kwargs):
        delete_id = kwargs['delete_id']
        print(delete_id)
        Instagram.objects.filter(id=delete_id).delete()
        return super().get_redirect_url()

# mirip antara create dan update

class SosmedFormView(View):
    template_name = 'sosmed/create.html'
    form =InstagramForm()
    mode=   None
    context ={}

    def get(self, *args, **kwargs):
        if self.mode == 'update':
            akun_update = Instagram.objects.get(id=kwargs['update_id'])
            data = akun_update.__dict__
            self.form = InstagramForm(initial= data, instance= akun_update)

        self.context = {
            "page_title":"Tambah akun",
            "akun_form":self.form,
        }

        return render(self.request, self.template_name, self.context)
    
    def post(self, *args, **kwargs):
        print(kwargs)

        if kwargs.__contains__('update_id'):
            akun_update = Instagram.objects.get(id=kwargs['update_id'])
            self.form = InstagramForm(self.request.POST, instance= akun_update)
        else :
            self.form = InstagramForm(self.request.POST)

        if self.form.is_valid():
            self.form.save()
        
        return redirect('sosmed:list')







# def delete(request, delete_id):
#     Instagram.objects.filter(id=delete_id).delete()
#     return redirect('sosmed:list')



# versi function
# def list(request):
#     semua_akun    = Instagram.objects.all()

#     context = {
#         'page_title':'sosial media',
#         'semua_akun':semua_akun,
#     }

#     return render(request, 'sosmed/list.html', context)


# def update(request, update_id):
#     akun_update = Instagram.objects.get(id=update_id)
#     data = {
#         'nama_depan'    :akun_update.nama_depan,
#         'nama_belakang' :akun_update.nama_belakang,
#         'username'      :akun_update.username,
#         'content'      :akun_update.content,
#     }
#     akun_form = InstagramForm(request.POST or None, initial=data, instance=akun_update)

#     if request.method == 'POST':
#         if akun_form.is_valid():
#             akun_form.save()

#         return redirect('sosmed:list')

#     context = {
#         "page_title": "Update akun",
#         "akun_form": akun_form,
#     }

#     return render(request, 'sosmed/create.html', context)


# def create(request):
#     akun_form = InstagramForm(request.POST or None)

#     if request.method == 'POST':
#         if akun_form.is_valid():
#             akun_form.save()

#         return redirect('sosmed:list')

#     context = {
#         "page_title": "Tambah akun",
#         "akun_form": akun_form,
#     }

#     return render(request, 'sosmed/create.html', context)

