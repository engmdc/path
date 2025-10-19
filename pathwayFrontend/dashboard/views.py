from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

# Authentication views
def login_view(request):
    if request.method == 'POST':
        # Print debug information
        print("POST request received in login_view")
        print("POST data:", request.POST)
        
        # In a real application, you would authenticate the user here
        # For now, we'll just redirect to the dashboard
        
        # Bypass the @login_required decorator by setting a session variable
        # This is just for demonstration purposes - in a real app you would authenticate properly
        request.session['authenticated'] = True
        
        # Use an explicit redirect to the index view
        response = redirect('index')
        print("Redirecting to:", response.url)
        return response
    
    context = {
        'segment': 'login'
    }
    return render(request, 'authentication/login.html', context)

def signup_view(request):
    context = {
        'segment': 'signup'
    }
    return render(request, 'authentication/signup.html', context)

# Main dashboard views
# Modified to use session authentication instead of Django's built-in auth
def index(request):
    # Check if the user is authenticated via session
    if not request.session.get('authenticated', False):
        # If not authenticated, redirect to login
        return redirect('login')
    
    context = {
        'segment': 'dashboard'
    }
    return render(request, 'dashboard/index.html', context)

# Modified to use session authentication
def profile(request):
    # Check if the user is authenticated via session
    if not request.session.get('authenticated', False):
        # If not authenticated, redirect to login
        return redirect('login')
    
    context = {
        'segment': 'profile'
    }
    return render(request, 'dashboard/profile.html', context)

# Logout view
def logout_view(request):
    # Clear the authenticated session variable
    if 'authenticated' in request.session:
        del request.session['authenticated']
    
    # Redirect to login page
    return redirect('login')
