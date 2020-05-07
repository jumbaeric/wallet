from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# home view.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'authenticate/dashboard.html', {})
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have Successfully Logged In')
                return render(request, 'authenticate/dashboard.html', {})
            else:
                messages.success(request, 'Log in Error')
                return render(request, 'authenticate/home.html', {})
        else:
            return render(request, 'authenticate/home.html', {})

# register view.
def register_user(request):
    if request.user.is_authenticated:
        return render(request, 'authenticate/dashboard.html', {})
    else:
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            if password1==password2:
                user = User.objects.create_user(username, email, password1)
                if user.objects.filter(username=username).exists():
                    messages.success(request, 'Username Exists')
                elif user.objects.filter(email=email).exists():
                    messages.success(request, 'Email Exists')
                else:
                    user.first_name = first_name
                    user.last_name = last_name
                    user.save()
                    messages.success(request, 'You have Registered Successfully')
            else:
                messages.success(request, 'Passwords do not match')
                return redirect('home')
        else:
            return render(request, 'authenticate/register.html', {})
    
# Logout User
def logout_user(request):
    logout(request)
    messages.success(request, 'You have been Logged out')
    return redirect('home')


def dashboard(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == 'POST':
            credit_amount = int(request.POST['credit_amount'])
            username = request.POST['username']
            if current_user.userprofile.credits < credit_amount:
                messages.success(request, 'You have insufficient Credit to Make the transfer')
                return redirect()
            else:
                current_user.userprofile.credits = current_user.userprofile.credits - credit_amount
                current_user.userprofile.save
                messages.success(request, 'You have Successfully Credited')
        users = User.objects.all()
        return render(request, 'authenticate/dashboard.html', {'users': users, 'current_user':current_user})
    else:
        return redirect('home')