from django.urls import path
from .views import RegisterHandler,LoginHandler,LogoutHandler


urlpatterns = [
    path("users/register/",RegisterHandler,name="register"),
    path("users/login/",LoginHandler,name="login"),
    path("users/logout/",LogoutHandler,name="logout")
]