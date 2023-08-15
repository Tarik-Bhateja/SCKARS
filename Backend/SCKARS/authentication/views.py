from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    # if User hits on /auth URL
    return redirect('login/')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('/dashboard/')  # Redirect to user profile page
    return render(request,"register-6.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard/')  # Redirect to user profile page
    return render(request,"login-6.html")

    
