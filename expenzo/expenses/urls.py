from django.urls import path
from . import views


app_name = "expenses"

urlpatterns = [
    path("<int:pk>/detail/", views.ExpenseDetailView.as_view(), name="detail"),
    path("create/", views.ExpenseCreateView.as_view(), name="create"),
    path("<int:pk>/update/", views.ExpenseUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.ExpenseDeleteView.as_view(), name="delete"),
    path("", views.ExpenseListView.as_view(), name="index")
]