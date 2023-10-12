from django.urls import path
from UsersApp import views

app_name = "users_app"

urlpatterns=[
    path("register",views.register,name='register'),
    path("user_login/",views.user_login,name='user_login')
]