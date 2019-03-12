from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm


def home_page(request):
    content = {
        "title": "Home",
        "content": "home page!",

    }
    return render(request, "home_page.html", content)


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
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, "register_page.html", content)


def about_page(request):
    content = {
        "title": "about",
        "content": "home page!",

    }
    return render(request, "home_page.html", content)


def contact_page(request):
    form = ContactForm(request.POST or None)
    content = {
        "title": "contact",
        "content": "home page!",
        "form": form,

    }
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "contact_page.html", content)
