from django.shortcuts import redirect, render

# Create your views here.
from .forms import PostForm
from .models import PostModel

def list(request):
    posts = PostModel.objects.all()

    context = {
        'page_title':'semua post',
        'posts':posts,
    }
    return render(request, 'blog/list.html', context)

def create(request):
    post_form = PostForm(request.POST or None)

    if request.method == 'POST': #post request dari browser/user
        if post_form.is_valid():
            post_form.save()

            return redirect('blog:list')
    
    context ={
        'page_title': 'Create post',
        'post_form': post_form,
    }
    return render(request, 'blog/create.html', context)