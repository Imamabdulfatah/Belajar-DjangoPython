# from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'judul':'motivasi inspirasi',
        'subjudul':'selamat datang',
        'banner' : 'img/banner_home.png',
    }
    return render(request,'index.html', context)

