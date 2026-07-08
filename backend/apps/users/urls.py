from django.urls import path
from .views import (
    RegisterView, 
    ProfileView,
    #LoginView,
    #RefreshTokenView,
)

urlpattersn =[
    path(
        "register/", 
        RegisterView.as_view(), 
        name="register"
    ),
    path(
        "profile/",
        ProfileView.as_view(),
        name="profile",
    ),
    path(
        "login/",
        LoginView.as_view(),
        name="login",
    ),
    path(
        "refresh/",
        RefreshTokenView.as_view(),
        name="refresh",
    ),
]