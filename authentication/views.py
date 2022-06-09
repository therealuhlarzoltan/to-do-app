import django
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.urls import reverse_lazy

from .forms import SignUpForm, UserUpdateForm


# Create your views here.
def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST or None)
        if form.is_valid():
            user_ = form.get_user()
            login(request, user_)
            return redirect("/")
        else:
            print("Errors:", form.errors)
    context = {
        "form": form,
        "btn_label": "Login",
        "title": "Login",
        "template_name":"components/login_form.html"
    }
    return render(request, "authentication/auth.html", context)

@login_required
def logout_view(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            logout(request)
            return redirect("/")
        context = {
            "form": None,
            "description": "Are you sure you want to logout?",
            "btn_label": "Click to Confirm",
            "title": "Logout",
            "template_name":"components/logout_form.html"
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
        "title": "Register",
        "template_name":"components/register_form.html"
    }
    return render(request, "authentication/auth.html", context)

@login_required
def profile_view(request):
    user = request.user
    form = UserUpdateForm(instance=user)
    if request.method == 'POST':
        print(request.POST)
        form = UserUpdateForm(request.POST or None, instance=user )
        if form.is_valid():
            form.save()
    return render(request, 'authentication/profile.html', {'form':form})


@login_required
def password_change_view(request):
    user = request.user
    form = PasswordChangeForm(user)
    context = {
        'title':'Password Change',
        'template_name':'components/password_change_form.html',
        'btn_label':'Change Password',
        'form':form
    }
    if request.method == 'POST':
        form = PasswordChangeForm(user, request.POST or None)
        if form.is_valid():
            form.save()
            logout(request)
            return redirect(reverse_lazy('login'))
        else:
            context['form'] = form
    return render(request, 'authentication/password.html', context)
