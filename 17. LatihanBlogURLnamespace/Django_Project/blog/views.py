# views blog
from django.shortcuts import render

from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    categories = Post.objects.values('category').distinct()
    context = {
        'Judul':'myBlog',
        'Content' : 'Jurnal MotivasiInspirasi',
        'Categories' :categories,
        'Posts': posts,
    }
    return render(request, 'blog/index.html',context)


def categoryPost(request, categoryInput):
    posts = Post.objects.filter(category=categoryInput)

    # mengambil nilai categories dan   distinct() untuk mengambil nilai unik
    categories = Post.objects.values('category').distinct()
    print(categories)
    
    context = {
        'Judul':'blog category',
        'Content' : 'Tampilkan Berdasarkan category',
        'Categories' :categories,
        'Posts': posts,
    }
    return render(request, 'blog/category.html',context)


def detailPost(request, slugInput):
    posts = Post.objects.get(slug=slugInput)
    categories = Post.objects.values('category').distinct()
    context = {
        'Judul':'Blog deskripsi',
        'Content' : 'ini adalah deskripsi Blog',
        'Categories' :categories,
        'Posts': posts,
    }
    return render(request, 'blog/detail.html',context)
