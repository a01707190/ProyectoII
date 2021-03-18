from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages
# import from local directory
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'home.html', {})


# Create your views here.
# Signup
def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created Successfully!!!')
            user = fm.save()

            login(request, user)
            return redirect('/')
    else:
        fm = SignUpForm()
    return render(request, 'signup.html', {'form': fm})


# Login
def login_request(request):
    if request.method =='POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            print(request.POST['username'])
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request,"login.html", {"form":form})


# Profile
def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'enroll/profile.html', {'name': request.user})
    else:
        return HttpResponseRedirect('/login/')


# Logout
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out succesfully')
    return redirect('/')
