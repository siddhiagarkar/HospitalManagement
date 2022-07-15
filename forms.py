from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password


class CreateUserForm(UserCreationForm):
    username = forms.CharField(required = True, label = "Name")
    email = forms.EmailField(required  = True, label = "Email ID") 

    class meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        def save(self, commit = True):
            user.email = self.cleaned_data['email']

            if commit:
                    user.save()
                    return user

class authform(AuthenticationForm):
    username = forms.CharField(required = True, label = "Loginname")
    password = forms.CharField(required = True, label = "Loginpassword")

    class meta:
        model = User
        fields = ('username', 'password1')

        def save(self, commit = True):
            user.password = self.cleaned_data['password1']

            if commit:
                    user.save()
                    return user
