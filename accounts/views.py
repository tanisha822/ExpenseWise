from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def signup_view(request):
    if request.method == "POST":
        first_name = request.POST["first_name"].strip()
        last_name = request.POST["last_name"].strip()
        email = request.POST["email"].strip()
        username = request.POST["username"].strip()
        password = request.POST["password"]

        if not first_name.isalpha():
            messages.error(request, "First name should contain only alphabets!")
            return redirect("signup")

        if not last_name.isalpha():
            messages.error(request, "Last name should contain only alphabets!")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect("signup")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect("signup")

        if len(password) < 8:
            messages.error(request, "Password must contain at least 8 characters!")
            return redirect("signup")

        User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password
        )

        messages.success(request, "Account created successfully!")
        return redirect("login")

    return render(request, "accounts/signup.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"].strip()
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("home")

        messages.error(request, "Invalid username or password!")
        return redirect("login")

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")