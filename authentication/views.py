from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

from .forms import SignUpForm


# Create your views here.
def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user_ = form.get_user()
        login(request, user_)
        return redirect("/")
    context = {
        "form": form,
        "btn_label": "Login",
        "title": "Login"
    }
    return render(request, "authentication/auth.html", context)


def logout_view(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            logout(request)
            return redirect("/")
        context = {
            "form": None,
            "description": "Are you sure you want to logout?",
            "btn_label": "Click to Confirm",
            "title": "Logout"
        }
    else:
        return redirect("/")
    return render(request, "authentication/auth.html", context)

def register_view(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=True)
        user.set_password(form.cleaned_data.get("password1"))
        login(request, user)
        return redirect("/auth/login")
    context = {
        "form": form,
        "btn_label": "Register",
        "title": "Register"
    }
    return render(request, "authentication/auth.html", context)