from django.shortcuts import render

def index(request):
    context = {
        'heading': 'home',
        'judul': 'home',
    }

    if request.method == 'POST':
        print("ini adalah method post")
        # sesuai dengan nama pada html input
        print(request.POST['nama'])
        context['nama'] = request.POST['nama']
        context['alamat'] = request.POST['alamat']
    else:
        print("ini adalah method get")
    
    print(request.POST)

    return render(request,'index.html',context)