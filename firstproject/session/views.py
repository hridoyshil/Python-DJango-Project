from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# Create your views here.


def loginuser(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("homeview")
            else:
                messages.error(request, "Invalid Username or password!")
        else:
            messages.error(request, "Invalid Username or password!")
    else:
        form = AuthenticationForm()
    return render(request, "session/login.html", {"form": form})


def logoutuser(request):
    logout(request)
    messages.success(request, "successfully logged out!")
    return redirect("homeview")


def registration(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            current_site = get_current_site(request)
            mail_subject = "Activate Your Account"
            message = render_to_string(
                "session/account.html",
                {
                    "user": user,
                    "domain": current_site.domain,
                },
            )
            send_mail = form.cleaned_data.get("email")
            email = EmailMessage(mail_subject, message, to=[send_mail])
            email.send()
            messages.success(request, "Successfully created account")
            return redirect("login")
    else:
        form = SignUpForm()
    return render(request, "session/signup.html", {"form": form})


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password successfully change")
            return redirect("homeview")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, "session/change_pass.html", {"form": form})
