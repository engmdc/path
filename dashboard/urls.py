from django.urls import path
from dashboard import views

urlpatterns = [
    # Authentication routes
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    
    # Dashboard routes
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
]
