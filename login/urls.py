from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name="home"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
]
