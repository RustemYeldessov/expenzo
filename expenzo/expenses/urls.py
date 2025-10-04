from django.urls import path

from expenzo.expenses import views

urlpatterns = [
    path('', views.ExpenseListView.as_view(), name='expenses_index'),
    path('create/', views.ExpenseCreateView.as_view(), name='expenses_create'),
    path(
        '<int:pk>/update/',
        views.ExpenseUpdateView.as_view(),
        name='expenses_update'
    ),
    path(
        '<int:pk>/delete/',
        views.ExpenseDeleteView.as_view(),
        name='expenses_delete'
    ),
    path('<int:pk>/', views.ExpenseDetailView.as_view(), name='expenses_show'),
]