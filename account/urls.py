from django.urls import path
from .views import login_user, logout_user, register_user

urlpatterns = [
    path("logout/", logout_user, name="logout_user"),
    path("", login_user, name="login_user"),
    path('register-user/', register_user, name="register_user")

]
