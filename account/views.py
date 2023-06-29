from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.
def login_user(request):
    if request.method == "POST":
        un = request.POST.get("username")
        pw = request.POST.get("password")
        user = authenticate(request, username=un, password=pw)
        if not user:
            return redirect("login_user")
        login(request, user)
        return redirect("crud_home")
    context = {
        "title": "Login User"
    }
    return render(request, "account/login.html", context=context)


def logout_user(request):
    logout(request)
    return redirect("login_user")


""" There are normally three types of Authentication:
=> basic Authentication
1.Session Authentication
2. Token Authentication
3. JWT Authentication (Json Web Token)

"""
def register_user(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        if password != repeat_password:
            return redirect("register_user")
        user = User.objects.create(username=username, first_name=first_name, last_name=last_name, email=email,
                                   is_staff=True)
        user.set_password(password)
        user.save()
        return redirect("login_user")
    context = {
        "title": "Register User"
    }
    return render(request, "account/register_user.html", context=context)