from django.urls import path, include

from expenzo.users import views

app_name = "users"

urlpatterns = [
    path("", views.UsersListView.as_view(), name="index"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
    path("create/", views.UsersCreateView.as_view(), name="create"),
    path(
        "<int:pk>/update/",
        views.UserUpdateView.as_view(),
        name="update"
    ),
    path(
        "<int:pk>/delete/",
        views.UserDeleteView.as_view(),
        name="delete"
    ),

    path("expenses/", include("expenzo.expenses.urls")),
]