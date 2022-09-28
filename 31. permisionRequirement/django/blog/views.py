from django.shortcuts import render

from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.


# lihat can_edit di models
# @permission_required('blog_can_edit')
def updateView(request):
    context ={
        'page_title':'edit Artikel',
    }
    return render(request, 'blog/edit.html', context)
# untuk permision sendiri/peruser jika di user masuuk blog|add
@permission_required('blog.add_artikel')

# melakukan forbiden terhadap user yg tidakbisa mengakses
# bisa double
@login_required
@permission_required('blog.add_edit', login_url=None, raise_exception=True)

# diawal akan masuk ke login
# @permission_required('blog.add_artikel', login_url='/admin/')
def addView(request):
    context ={
        'page_title':'Add Artikel',
    }
    return render(request, 'blog/add.html', context)

def indexView(request):
    print(request.user.get_all_permissions())
    context ={
        'page_title':'Blog',
    }
    return render(request, 'blog/index.html', context )
