from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
]