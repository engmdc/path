from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.utils.decorators import method_decorator
from .forms import LoginForm, SignUpForm

# Create your views here.

# Authentication views
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            remember_me = form.cleaned_data.get('remember_me')
            user = authenticate(username=username, password=password)
            if user is not None:
                # If remember_me is False, set session expiry to 0 (close browser logout)
                if not remember_me:
                    request.session.set_expiry(0)
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
        
    context = {
        'segment': 'login',
        'form': form
    }
    return render(request, 'authentication/login.html', context)

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
        
    context = {
        'segment': 'signup',
        'form': form
    }
    return render(request, 'authentication/signup.html', context)

# Main dashboard views
@login_required
def index(request):
    context = {
        'segment': 'dashboard'
    }
    return render(request, 'dashboard/index.html', context)

@login_required
def profile(request):
    context = {
        'segment': 'profile'
    }
    return render(request, 'dashboard/profile.html', context)

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')
