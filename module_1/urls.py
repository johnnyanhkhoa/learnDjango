from argparse import Namespace
from django.urls import path, re_path
from module_1 import views

app_name = "module_1"
urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("create_rifle/", views.create_rifle, name="create_rifle"),
    path(
        "create_author_and_book/",
        views.create_author_and_book,
        name="create_author_and_book",
    ),
    path("view_book/", views.view_book, name="view_book"),
    path("view_rifle/", views.view_rifle, name="view_rifle"),
    path("search/", views.search, name="search"),
]
