from django.shortcuts import render ,HttpResponse , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login , logout

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
            return HttpResponse("Password and Confirm Password Must be Same")
        elif User.objects.filter(username=username).exists():
            return HttpResponse("Username already taken")
        elif User.objects.filter(email=email).exists():
            return HttpResponse("email already taken")

        elif username =='':
            return HttpResponse("username is none please enter correct username ")

        else :
            user = User.objects.create_user(username=username , email=email , password=password1)
            user.first_name = f_name
            user.last_name = l_name
            user.save()
            return HttpResponse("User Created successfully please login")

    else:
        return render(request, 'register.html')

def signin(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request , user)
            return HttpResponse("Signin Successfully")
        else:
            return HttpResponse("Wrong Credentials")
    else : 
        return render(request , "signin.html")


def signout(request):
    logout(request)
    return HttpResponse("logout successfully")

def authredirect(request):
    return redirect("home")