# from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'Judul':'motivasi inspirasi',
        'Content':'Ini adalah halaman home',
    }
    return render(request,'index.html', context)

