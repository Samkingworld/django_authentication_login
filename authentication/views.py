from django.http import HttpResponse 
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return  render(request, "authentication/index.html")


def signup(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2 :
            myuser = User.objects.create_user(username=username, email=email, password= pass1)
            myuser.first_name = fname
            myuser.last_name = lname

            myuser.save()

            messages.success(request=request, message='You have successfully created an account')
            return redirect('signin')
        
        elif pass1 != pass2:
            return HttpResponse('Your Password do not match please try again')
        
    return render(request, 'authentication/signup.html')

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render (request, 'authentication/index.html', {'fname':fname})
        else:
            messages.error(request, message='Bad Credentials')
            return redirect('home')

        

    return render(request, 'authentication/signin.html')

def signout(request):
    logout(request)
    messages.success(request, "Logged out Successfully!")
    return redirect('home')
