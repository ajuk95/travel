from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages, auth

# Create your views here.
def logout(request):
    auth.logout(request)
    print("user logged out")
    return redirect('/')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print(user, "user logged in")
            return redirect('/')
        else:
            print("invalid user credentials")
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, 'login.html')

def register(request):
    # return HttpResponse("hi")
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=firstname, last_name=lastname, email=email)
                user.save()
                print("user registered:", user)
                return redirect('login')
        else:
            messages.info(request, "passwords not matching")
            print("passwords not matching")
            return redirect('register')
        # return redirect('/')
    return render(request, "register.html")
