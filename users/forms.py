from django.contrib.auth.forms import AuthenticationForm,UsernameField,UserChangeForm,UserCreationForm,PasswordChangeForm
from django import forms
from .models import User
from django.utils.translation import gettext_lazy as _


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True,"class":"form-control"}), label = "Username or Email address")
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password","class":"form-control"}),
    )

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password","class":"form-control"}),
        # help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password","class":"form-control"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
        widgets = {
            "first_name":forms.TextInput(attrs = {"class":"form-control"}),
            "last_name":forms.TextInput(attrs = {"class":"form-control"}),
            "username":forms.TextInput(attrs = {"class":"form-control"}),
            "email":forms.TextInput(attrs = {"class":"form-control"}),
        }
            
class EditForm(forms.ModelForm):
    email_displayed = forms.BooleanField(label = "Display email in profile page", required=False)
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email',"email_displayed"]


class ChangePasswordForm(PasswordChangeForm):
    pass
        
