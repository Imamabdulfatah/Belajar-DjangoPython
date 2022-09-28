# views blog
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul':'Blog',
        'subjudul' : 'Jurnal MotivasiInspirasi',
        'kontributor':'imam abdul',
        'banner':'blog/img/banner_blog.png',
    }
    return render(request, 'blog/index.html',context)

def news(request):
    context = {
        'judul':'blog',
        'kontributor':'asep',
    }
    return render(request, 'blog/index.html',context)

def cerita(request):
    context = {
        'judul':'blog',
        'kontributor':'abdul',
    }
    return render(request, 'blog/index.html',context)