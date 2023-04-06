from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('sign-up/', views.signup, name='sign-up'),
    path('sign-in/', auth_views.LoginView.as_view(template_name='accounts/signin.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]