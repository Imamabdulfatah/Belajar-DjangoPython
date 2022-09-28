from django.shortcuts import render

def index(request):
    context = {
        'page_title':'home',
    }
    return render(request,'index.html',context)