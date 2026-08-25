"""
URL configuration for myfirstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myfirstproject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('Home/', views.Home, name='home'),
    path('Aboutus/', views.Aboutus),
    path('contactus/', views.contactus),
    path('Services/', views.Services),
    path('Gallery/', views.Gallery),
    path('blog/', views.blog),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
   
]

