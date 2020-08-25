from django.shortcuts import render
from basic_app.forms import userForm,userProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
# Create your views here.
######################################### INDEX
def index(request):
    return render(request,'basic_app/index.html')
######################################### LogOut
@login_required
def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
######################################### Special
@login_required
def special(request):
    return HttpResponse("You are logged in, nice!")
######################################### REGISTER
def register(request):
    registered = False
    if request.method == "POST":
        userFormreg = userForm(data=request.POST)
        profileFormreg = userProfileInfoForm(data=request.POST)

        if userFormreg.is_valid() and profileFormreg.is_valid():
            user = userFormreg.save()
            user.set_password(user.password)
            user.save()

            profile = profileFormreg.save(commit=False)
            profile.user = user

            if 'profilePic' in request.FILES:
                profile.profile_pic = request.FILES['profilePic']

            profile.save()

            registered = True
        else:
            print("userFormreg.errors,profileFormreg.errors")
    else:
        userFormreg = userForm()
        profileFormreg = userProfileInfoForm()
    return render(request,'basic_app/registration.html',
                                                        {'userFormreg':userFormreg,
                                                        'profileFormreg':profileFormreg,
                                                        'registered':registered})
######################################### logIN
def userLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Your account is inactive")
        else:
            print("Someone tried to log in and failed")
            print("Username:{} and password {}".format(username,password))
            return HttpResponse("invalid login details supplied")
    else:
        return render(request,'basic_app/login.html',{})
