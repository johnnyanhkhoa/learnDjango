from argparse import Namespace
from django.urls import path, re_path
from module_1 import views

app_name = 'module_1'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('create_rifle/', views.create_rifle, name='create_rifle'),
    
]
