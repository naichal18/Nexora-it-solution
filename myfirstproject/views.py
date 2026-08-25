from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

def Home(request):
    return render(request, 'index.html')

def Aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')

def Services(request):
    return render(request, 'services.html')

def Gallery(request):
    return render(request, 'gallery.html')

def blog(request):
    return render(request, 'blog.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        return render(request, 'login.html', {'error': 'Invalid username or password.'})

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')




    
  