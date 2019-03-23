from django.shortcuts import render
from . forms import ContactForm
from . models import ContactModel
from django.contrib import messages


# Create your views here.


def contact(request):
    form = ContactForm(request.POST or None)
    content = {
        "title": "contact",
        "content": "home page!",
        "form": form,

    }
    if form.is_valid():
        print(form.cleaned_data)
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        email = form.cleaned_data.get("email")
        message = form.cleaned_data.get("message")
        query = ContactModel.objects.create(first_name=first_name, last_name=last_name, email=email, message=message)
        messages.error(request, 'You message has been submitted')
        print(form.cleaned_data)
    return render(request, "contact_page.html", content)
