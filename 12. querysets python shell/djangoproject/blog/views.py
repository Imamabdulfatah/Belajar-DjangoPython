from django.shortcuts import render

# Create your views here.

from .models import Post

def index(request):
    posts = Post.objects.all()
    context = {
        'Title' : 'Blog',
        'Heading' : 'Blog di my website',
        'Category' : 'All',
        'Posts':posts,
    }

    return render(request,'blog/index.html',context)



def berita(request):
    posts = Post.objects.filter(category='blog')
    context = {
        'Title' : 'Blog',
        'Heading' : 'Blog di my website',
        'Category' : 'berita',
        'Posts':posts,
    }

    return render(request,'blog/index.html',context)



def jurnal(request):
    posts = Post.objects.filter(category='blog')
    context = {
        'Title' : 'Blog',
        'Heading' : 'Blog di my website',
        'Category' : 'jurnal',
        'Posts':posts,
    }
    return render(request,'blog/index.html',context)


def gosip(request):
    posts = Post.objects.filter(category='gosip')
    context = {
        'Title' : 'Blog',
        'Heading' : 'Blog di my website',
        'Category' : 'gosip',
        'Posts':posts,
    }

    return render(request,'blog/index.html',context)
