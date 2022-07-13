from distutils.log import Log
from django.shortcuts import render
from django.urls import reverse_lazy

from posts.models import BlogPost, Profile
from .forms import PostForm,ProfileForm
from django.views.generic import CreateView,ListView,FormView,DetailView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


#posts model
class CreatePost(LoginRequiredMixin,FormView):
    form_class = PostForm
    template_name = "posts/blogpost_create.html"
    success_url = reverse_lazy("posts:home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class HomeView(ListView):
    model = BlogPost
    context_object_name = "latest_posts"
    template_name = "posts/home.html"
    ordering = ['-date_updated']


class EditPostView(LoginRequiredMixin,UpdateView):
    form_class = PostForm
    model = BlogPost
    template_name = "posts/update_post.html"


class DeletePost(DeleteView):
    model = BlogPost
    template_name = "posts/delete_post.html"


#profile model
class ProfileView(LoginRequiredMixin,DetailView):
    model = Profile
    context_object_name = "profile"
    template_name = "posts/profile.html"
    slug_field = "user__username"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = BlogPost.objects.filter(user = self.request.user).order_by("-date_updated")
        return context

class EditProfileView(LoginRequiredMixin,UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "posts/edit_profile.html"



