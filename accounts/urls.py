from django.urls import path
from accounts import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.inicioAccounts, name='inicioAccounts'),
    path("login/", views.login_request, name='loginAccounts'),
    path("singup/", views.singup_request, name='singupAccounts'),
    path("logout/", LogoutView.as_view(template_name='accounts/logout.html'), name='logoutAccounts'),
    path("profile/", views.edit_request, name='profileAccounts'),
]