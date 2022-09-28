from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul':'About motivasi inspirasi',
        'subjudul':'tentang motivasi inspirasi',
        'banner':'about/img/banner_about.png',
    }
    return render(request,'about/index.html',context)
