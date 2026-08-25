from django.shortcuts import render , redirect

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
    error = ""

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == "admin" and password == "123":
            return redirect('/Home/')
        else:
            error = "Invalid Username or Password"

    return render(request, 'login.html', {'error': error})




    
  