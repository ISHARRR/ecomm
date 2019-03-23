from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name",}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name",}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Full Name",}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Message",}))
