from django.contrib import admin
from django.urls import path
from band_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("members/", views.band_members, name="members"),
    path("events/", views.events, name="events"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
]
