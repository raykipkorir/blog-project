from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


app_name = "users"
urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name = "login"),    
    path('logout/', LogoutView.as_view(), name = "logout"),    
    path('signup/', views.signup, name = "signup"),    
    path("delete_user/<int:pk>/",views.DeleteUser.as_view(), name = "delete_user"),
    path("edit_user/<int:pk>/",views.EditUser.as_view(), name = "edit_user"),
    # path("changepassword/<int:pk>/",views.ChangePassword.as_view(), name = "change_password")
    path("changepassword/",views.changepassword, name = "change_password")
]
