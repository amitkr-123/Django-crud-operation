from django.shortcuts import render ,HttpResponse , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login , logout
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method =='POST':
        username =  request.POST['username']
        email =  request.POST['email']
        f_name =  request.POST['f_name']
        l_name =  request.POST['l_name']
        password1 =  request.POST['password1']
        password2 =  request.POST['password2']

        if password1 != password2:
            messages.success(request , "Password and Confirm Password Must be Same")
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.success(request , "Username already taken")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.success(request , "email already taken")
            return redirect('register')

        elif username =='':
            messages.success(request , "username is none please enter correct username ")
            return redirect('register')

        else :
            user = User.objects.create_user(username=username , email=email , password=password1)
            user.first_name = f_name
            user.last_name = l_name
            user.save()
            messages.success(request ,  "User Created successfully please login")
            return redirect('register')

    else:
        return render(request, 'register.html')

def signin(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request , user)
            messages.success(request , "Signin Successfully")
            return redirect('home')
        else:
            messages.error(request , "Wrong Credentials")
            return redirect('signin')
    elif request.user.is_authenticated:
        messages.success(request , "User already authenticated") 
        return redirect('home')
    else : 
        return render(request , "signin.html")

def signout(request):
    logout(request)
    messages.success(request , "logout successfully")
    return redirect("home")

def authredirect(request):
    if request.user.is_authenticated :
        messages.success(request , "User already authenticated") 
        return redirect('home')
    else :
        return redirect('signin')
    