from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse,reverse_lazy
from django.views.generic import DeleteView,UpdateView
from users.forms import ChangePasswordForm, LoginForm,SignUpForm,EditForm
from django.contrib.auth import authenticate,login,update_session_auth_hash
from django.contrib.messages.views import SuccessMessageMixin
from users.models import User
from django.contrib import messages


class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = LoginForm
    redirect_authenticated_user = True
    success_message = "Successfully logged in"


def signup(request):
    if not request.user.is_authenticated:

        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(request, username = username, password = password)
                if user is not None:
                    login(request,user)
                    messages.success(request, "Account created successfully")
                    return redirect("posts:home")
        else:
            form = SignUpForm()

        context = {"form":form}
        return render(request, "registration/signup.html", context)
    return redirect("posts:home")

# class ChangePassword(UpdateView):
#     model = User
#     form_class = ChangePasswordForm
#     template_name = "registration/changepassword.html"
#     success_url = reverse_lazy("users:login")

def changepassword(request):
    
    if request.method == "POST":
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user =form.save()
            update_session_auth_hash(request,user)
            messages.success(request, "Password Changed successfully")
            return redirect("posts:profile" ,slug = request.user.username)
    else:
        form = ChangePasswordForm(request.user)
    return render(request, "registration/changepassword.html",{"form":form})

class EditUser(SuccessMessageMixin, LoginRequiredMixin,UpdateView):
    model = User
    template_name = "registration/edit_user.html"
    form_class = EditForm
    success_message = "Account updated successfully"

class DeleteUser(SuccessMessageMixin, LoginRequiredMixin,DeleteView):
    model = User
    template_name = "registration/delete_user.html"
    success_url = reverse_lazy("users:login")
    success_message = "We are sad to see you leave :("
    
