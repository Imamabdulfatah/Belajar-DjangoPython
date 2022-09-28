# views blog
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul':'blog',
        'kontributor':'imam abdul',
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