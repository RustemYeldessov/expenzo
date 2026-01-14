from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import IndexView

urlpatterns = [
    path("admin/", admin.site.urls),

    path("users/", include(("expenzo.users.urls", "users"), namespace="users")),
    path("categories/", include(("expenzo.categories.urls", "categories"), namespace="categories")),
    path("sections/", include(("expenzo.sections.urls", "sections"), namespace="sections")),

    path("", IndexView.as_view(), name='index'),
]
