from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Artikel

# Create your views here.
class ArtikelKategoriListView(ListView):
    model = Artikel
    template_name= "artikel/artikel_kategori_list.html"
    context_object_name = 'artikel_list'
    ordering = ['-published']
    paginate_by = 3

    def get_queryset(self):
        self.queryset = self.model.objects.filter(kategori=self.kwargs['kategori'])
        return super().get_queryset()

    def get_context_data(self, *args, **kwargs):
        # distict digunakan agagr tidak double
        # exclude mengambil sisa
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct().exclude(kategori=self.kwargs['kategori'])
        self.kwargs.update({'kategori_list': kategori_list})
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)



class ArtikelListView(ListView):
    model = Artikel
    template_name = "artikel/artikel_list.html"
    # memberi nama
    context_object_name= 'artikel_list'
    # mengurutkan  dan mengunakan - urutan akan terbalik
    ordering = ['-published']
    # memberi pagination kelompok angka
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        # distict digunakan agagr tidak double
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
        self.kwargs.update({'kategori_list': kategori_list})
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)

class ArtikelDetailView(DetailView):
    model = Artikel
    template_name = "artikel/artikel_detail.html"
    context_object_name = 'artikel'

    def get_context_data(self, *args, **kwargs):
        # distict digunakan agagr tidak double
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
        self.kwargs.update({'kategori_list': kategori_list})

        artikel_serupa = self.model.objects.filter(kategori= self.object.kategori).exclude(id=self.object.id)
        self.kwargs.update({'artikel_serupa':artikel_serupa})

        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)
