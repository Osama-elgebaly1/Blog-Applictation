from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .forms import SignUpForm,LoginForm,ChangePasswordForm,ProfileForm
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required


@login_required 
def profile(request):
    user = request.user
    profile = user.profile
    if request.method == 'POST':
            form = ProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request,'Your info has been updated.')
                return redirect('home')
    else:
        form = ProfileForm(instance=profile)
        return render(request,'pages/profile.html',{'form':form})
    


def out(request):
    logout(request)
    messages.success(request,'Logged out Successfully...')
    return redirect('home')


def update_password(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = ChangePasswordForm(user , request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Your password has been updated...')
                login(request,user)
                return redirect('home')
            else:
                for error in list(form.errors.values()):
                    messages.success(request,error)
                return redirect('update_password')
        else:
            form = ChangePasswordForm(user)
            return render(request,'pages/update_password.html',{'form':form})
    else:
        messages.success(request,'You must be logged in to access that page...')
        return redirect('login')


def log(request):
    # Checking if authenticated already 
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in !')
        return redirect('home')
    
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Check if the user existed 
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,'Logged in Successfully ...')
                return redirect('home')
            else:
                messages.error(request,'User is not existed !!')
                return redirect('login')
        else:
            messages.error(request,'Username Or Password is wrong !!')
            return redirect('login')
    else:
        form = LoginForm()
        return render(request,'pages/login.html',{'form':form})
    

            


def register(request):
    # Checking if the user has account already 
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in!')
        return redirect('home')
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # Checking if the data valid
        if form.is_valid():
            form.save()
            # log the user in 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,'Registerred Successfully ...')
            return redirect('home')
        else:
            redirect('register')
    
    # passing the form if the method is Get 
    form = SignUpForm()
    return render(request,'pages/register.html',{'form':form})
















    
    








    


