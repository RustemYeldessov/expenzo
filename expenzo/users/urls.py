from django.urls import path, include

from expenzo.users import views


urlpatterns = [
    path("", views.UsersListView.as_view(), name="users_index"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
    path("create/", views.UsersCreateView.as_view(), name="users_create"),
    path(
        "<int:pk>/update/",
        views.UserUpdateView.as_view(),
        name="users_update"
    ),
    path(
        "<int:pk>/delete/",
        views.UserDeleteView.as_view(),
        name="users_delete"
    ),

    path("expenses/", include("expenzo.expenses.urls")),
]