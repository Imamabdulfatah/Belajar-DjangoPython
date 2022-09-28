from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from django.contrib.auth import authenticate, login, logout

class IndexView(TemplateView):
    template_name = "index.html"



def index(request):
    context = {
        'page_title':'home',
    }
    # melihat data yang ada direquest
    # print(dir(request))
    # melihat usr
    # print(request.user)
    
    return render(request, "index.html", context)

def loginView(request):
    context = {
        'page_title':'Login',
    }

    if request.method == "POST":
        username_login = request.POST['username']
        password_login = request.POST['password']
       
        user = authenticate(request, username= username_login, password= password_login)
        
        if user is not None:
            login(request, user) 
            return redirect('index')
        else:
            return redirect('login')

        
    # username_udin = 'Udin'
    # password_udin = 'Imam1234'
    # user = authenticate(request, username= username_udin, password= password_udin)
    # print(user)

    # login(request,user)
    return render(request, 'login.html', context)

def logoutView(request):
    context={
        'page_title':'logout',
    }

    if request.method == "POST":
        if request.POST["logout"] == "Submit":
            logout(request)

        return redirect('index')


    return render(request,'logout.html', context)
