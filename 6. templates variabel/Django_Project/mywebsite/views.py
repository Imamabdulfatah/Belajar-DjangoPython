# from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'judul':'kelas umum',
        'kontributor':'imam',
    }
    return render(request,'index.html', context)

def about(request):
    return render(request,'about.html')