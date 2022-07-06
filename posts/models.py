from django.db import models
from blog import settings
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    url = models.URLField(blank=True)

    def get_absolute_url(self):
        return reverse("posts:edit_profile", kwargs={"pk": self.pk})
    


class BlogPost(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    slug = models.SlugField(blank = True)
    content =models.TextField()
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def get_absolute_url(self):
        return reverse("posts:edit_post", kwargs={"pk": self.pk})