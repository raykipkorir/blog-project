from django.urls import path
from . import views


app_name = "posts"
urlpatterns = [
    path("createpost/", views.CreatePost.as_view(), name="create_post"),
    path("home/", views.HomeView.as_view(), name="home"),
    path("editpost/<int:pk>/", views.EditPostView.as_view(), name="edit_post"),
    path("deletepost/<int:pk>/", views.DeletePost.as_view(), name="delete_post"),
    path("<slug>/", views.ProfileView.as_view(), name="profile"),
    path("editprofile/<int:pk>/", views.EditProfileView.as_view(), name="edit_profile"),
]
