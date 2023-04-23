from django import forms
from account.models import User


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=250)
    password = forms.CharField(widget=forms.PasswordInput())


class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]
