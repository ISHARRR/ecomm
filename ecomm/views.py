from django.contrib.auth import authenticate, login, get_user_model, update_session_auth_hash
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
# from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from . forms import UpdateProfile


def login_page(request):
    form = LoginForm(request.POST or None)
    content = {
        "title": "login",
        "form": form,
    }
    if form.is_valid():

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            content['form'] = LoginForm()
            return redirect("/")
        else:
            print("error")
            messages.error(request, 'Incorrect password or username')
    return render(request, "login_page.html", content)


User = get_user_model()


def register_page(request):
    form = RegisterForm(request.POST or None)
    content = {
        "title": "register",
        "form": form,

    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
        print(new_user)
        return redirect("login")
    return render(request, "register_page.html", content)


def about(request):
    content = {
        "title": "about",
    }
    return render(request, "about.html", content)


@login_required()
def profile(request):
    args = {'user': request.user}
    return render(request, 'profile.html', args)


@login_required()
def update_profile(request):
    if request.method == 'POST':
        form = UpdateProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UpdateProfile(instance=request.user)
        args = {'form': form}
        return render(request, 'update_profile.html', args)


@login_required()
def update_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
        else:
            messages.error(request, 'Invalid password')
            return redirect('update_password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'change_password.html', args)
