from django.urls import path
from .views import (RegisterHandler,LoginHandler,LogoutHandler,ListandCreateHandler,
                    RetrieveUpdateDeleteHandler)


urlpatterns = [
    path("users/register/",RegisterHandler,name="register"),
    path("users/login/",LoginHandler,name="login"),
    path("users/logout/",LogoutHandler,name="logout"),
    path("books/",ListandCreateHandler,name="listandcreate"),
    path("books/<str:isbn>/",RetrieveUpdateDeleteHandler,name="retrieveupdatedelete"),
]