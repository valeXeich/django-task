from django.urls import path
from django.contrib.auth.views import LogoutView
from django.views.decorators.csrf import csrf_exempt

from .views import MainView, LoginView, SignUpView, UserInfo

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('login', LoginView.as_view(), name='login'),
    path('sign-up', csrf_exempt(SignUpView.as_view()), name='sign-up'),
    path('profile', UserInfo.as_view(), name='profile'),
    path('logout', LogoutView.as_view(), name='logout'),
]