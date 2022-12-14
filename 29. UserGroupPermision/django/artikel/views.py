from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group

# Create your views here.

# custom check
# jika dikhusus kan akun otong
@user_passes_test(lambda user:user.username == 'otong')
def otongView(request):
    return render(request , 'artikel/otong.html', {})

# simple decoratorcheck
# arti lambda sama dengan fungsi add 1
@user_passes_test(lambda user: Group.objects.get(name='penulis') in user.groups.all())
def artikelAddView2(request):
    context = {
        'page_title': 'tambah artikel view',
    }
    return render(request, 'artikel/artikel_add.html', context)


# decorator
def checkPenulis(user):
    test_group = Group.objects.get(name='penulis')
    user_group = user.groups.all()

    status = test_group in user_group
    print(status)
    return status



@user_passes_test(checkPenulis)
def artikelAddView(request):
    context = {
        'page_title': 'tambah artikel view',
    }
    return render(request, 'artikel/artikel_add.html', context)

# internal check
def artikelIndexView(request):
    context = {
        'page_title':'Artikel',
    }

    test_group = Group.objects.get(name='penulis')
    user_group = request.user.groups.all()

    if test_group in user_group:
        # logika untuk user dalam group
        template_name = 'artikel/index_penulis.html'
    
    else:
        # logika untuk user diluar group
        template_name = 'artikel/index_pembaca.html'


    return render(request, template_name, context)