from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Full Name",
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "class": "form-control",
            "placeholder": "Full Name",
        }
    ))

    content = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Message",
        }
    ))


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Username",
        }))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "class": "form-control",
            "placeholder": "Full Name",
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control"}), label='Confirm password',)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        queryset = User.objects.filter(username=username)
        if queryset.exists():
            raise forms.ValidationError("Username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('username')
        queryset = User.objects.filter(username=email)
        if queryset.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError("Passwords do not match")
        return data
