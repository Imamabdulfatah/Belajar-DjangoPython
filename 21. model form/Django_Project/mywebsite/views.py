from django.shortcuts import render

def index(request):
    context = {
        'page_judul':'motivasi inspirasi'
    }

    return render(request, 'index.html', context)