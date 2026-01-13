from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import IndexView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexView.as_view(), name='index'),

    path("users", include(("expenzo.users.urls", "users"), namespace="users")),
]
