from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    if request == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)

        if user is not None :
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credientials')
    else:
        return render(request, 'login.html')
    

def register(request):
    if request.method == 'POST':
        first_name = request.method['first_name']
        last_name = request.method['last_name']
        username = request.method['username']
        password1 = request.method['password1']
        password2 = request.method['password2']
        email = request.method['email']

        if password1 == password2:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email)
            user.save()
            print("user created")
    else:
        return render(request,'register.html')