# Pathway Frontend - Authentication Implementation

This README documents the implementation of login and logout functionality in the Pathway Frontend application.

## Table of Contents
1. [Overview](#overview)
2. [Login Implementation](#login-implementation)
3. [Logout Implementation](#logout-implementation)
4. [File Changes](#file-changes)
5. [Testing](#testing)

## Overview

The authentication system uses Django's session framework to manage user authentication state. Instead of using Django's built-in authentication system, we implemented a simplified session-based approach for demonstration purposes.

## Login Implementation

The login functionality follows these steps:

1. User enters email and password on the login page
2. Form is submitted to the server
3. Server sets an authentication flag in the session
4. User is redirected to the dashboard

### Key Components

- **Session Variable**: `request.session['authenticated'] = True` is used to mark a user as authenticated
- **Form Submission**: The login form submits via POST to the login view
- **Redirection**: After successful login, user is redirected to the dashboard index page

## Logout Implementation

The logout functionality follows these steps:

1. User clicks the logout link in the navigation menu
2. Server removes the authentication flag from the session
3. User is redirected back to the login page

## File Changes

### 1. Login View (`dashboard/views.py`)

```python
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
```

### 2. Dashboard View (`dashboard/views.py`)

```python
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
```

### 3. Profile View (`dashboard/views.py`)

```python
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
```

### 4. Logout View (`dashboard/views.py`)

```python
# Logout view
def logout_view(request):
    # Clear the authenticated session variable
    if 'authenticated' in request.session:
        del request.session['authenticated']
    
    # Redirect to login page
    return redirect('login')
```

### 5. URL Configuration (`dashboard/urls.py`)

```python
urlpatterns = [
    # Authentication routes
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    
    # Dashboard routes
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
]
```

### 6. Login Form Template (`templates/authentication/login.html`)

```html
<form id="login-form" action="" method="post">
{% csrf_token %}
    <div class="position-relative mb-4">
        <span class="form-icon">
            <!-- Email icon SVG -->
        </span>
        <input type="email" class="form-control form-control-lg ps-5" id="email" placeholder="Email address" required autofocus>
    </div>
    
    <div class="position-relative mb-4">
        <span class="form-icon">
            <!-- Password icon SVG -->
        </span>
        <input type="password" class="form-control form-control-lg ps-5" id="password" placeholder="Password" required>
    </div>
    
    <div class="d-flex justify-content-between align-items-center mb-4">
        <div class="form-check">
            <input class="form-check-input" type="checkbox" id="remember">
            <label class="form-check-label" for="remember">
                Remember me
            </label>
        </div>
        <a href="#" class="text-decoration-none link-light">Forgot password?</a>
    </div>
    
    <button type="submit" class="btn btn-login w-100" id="login-button">Sign in</button>
</form>
```

### 7. Login Form JavaScript (`templates/authentication/login.html`)

```javascript
// Handle login form submission
document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('login-form');
    
    if (loginForm) {
        // Update the form action to ensure it submits to the correct URL
        loginForm.action = window.location.pathname;
        
        // Add a submit event listener to show loading state
        loginForm.addEventListener('submit', function(e) {
            // Don't prevent default - we want the form to actually submit
            
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            
            // Validate form fields
            if (email && password) {
                // Show loading state on button
                const submitButton = document.querySelector('.btn-login');
                submitButton.textContent = 'Signing in...';
                submitButton.disabled = true;
                
                // Let the form submit naturally to the server
                return true;
            } else {
                // If validation fails, prevent submission
                e.preventDefault();
                alert('Please enter both email and password');
                return false;
            }
        });
    }
});
```

### 8. Navigation Template with Logout Link (`templates/includes/navigation.html`)

```html
<div class="dropdown-menu dashboard-dropdown dropdown-menu-end mt-2 py-1">
    <a class="dropdown-item d-flex align-items-center" href="#">
        <svg class="dropdown-icon text-gray-400 me-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-6-3a2 2 0 11-4 0 2 2 0 014 0zm-2 4a5 5 0 00-4.546 2.916A5.986 5.986 0 0010 16a5.986 5.986 0 004.546-2.084A5 5 0 0010 11z" clip-rule="evenodd"></path>
        </svg>
        My Profile
    </a>
    <div role="separator" class="dropdown-divider my-1"></div>
    <a class="dropdown-item d-flex align-items-center" href="{% url 'logout' %}">
        <svg class="dropdown-icon text-danger me-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path>
        </svg>                
        Logout
    </a>
</div>
```

### 9. Project Settings (`pathfrontend/settings.py`)

```python
# Authentication settings
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'login'
```

### 10. Main URLs Configuration (`pathfrontend/urls.py`)

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    # Root URL is now handled by dashboard.urls
]
```

## Testing

### Login Testing
1. Navigate to the login page (`/login/`)
2. Enter any email and password
3. Click the "Sign in" button
4. You should be redirected to the dashboard

### Logout Testing
1. While on any dashboard page, click on the user profile dropdown in the top-right corner
2. Click the "Logout" option
3. You should be redirected back to the login page

## Security Considerations

This implementation is for demonstration purposes only. In a production environment, you should:

1. Use Django's built-in authentication system or a secure third-party solution
2. Implement proper password hashing and validation
3. Add CSRF protection (already included in Django forms)
4. Consider implementing rate limiting for login attempts
5. Use HTTPS for all authentication-related traffic

## Future Improvements

- Implement proper user authentication with database storage
- Add password reset functionality
- Implement remember me functionality
- Add multi-factor authentication
- Implement social login options
