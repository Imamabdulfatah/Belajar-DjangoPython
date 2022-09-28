from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
#  view method dengan internal permision checks
def index(request):
    context = {
        'page_title':'home',
    }

    print(request.user.is_authenticated)
    
    template_name = None
    if request.user.is_authenticated:
        # logika untuk user
        template_name = 'index_user.html'
    else:
        # logika untuk anonymous user
        template_name = 'index_anonymous.html'
    
    return render(request, template_name, context)

def loginView(request):
    context = {
        'page_title':'Login',
    }
    if request.method == "GET":
        if request.user.is_authenticated:
            # logic untuk user
            return redirect('index')
        else:
            # logic untuk anonymous
            return render(request, 'login.html', context)

    if request.method == "POST":
        username_login = request.POST['username']
        password_login = request.POST['password']
       
        user = authenticate(request, username= username_login, password= password_login)
        
        if user is not None:
            login(request, user) 
            return redirect('index')
        else:
            return redirect('login')

    


@login_required
def logoutView(request):
    context={
        'page_title':'logout',
    }

    if request.method == "POST":
        if request.POST["logout"] == "Submit":
            logout(request)

        return redirect('index')


    return render(request,'logout.html', context)
