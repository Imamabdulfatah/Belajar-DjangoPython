from django.shortcuts import render

def index(request):
    context = {
        'heading':'Home',
        'content': 'ini adalah content',
    }

    return render(request,'index.html', context)