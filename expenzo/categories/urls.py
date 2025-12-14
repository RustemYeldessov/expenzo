from django.urls import path
from . import views


urlpatterns = [
    path('', views.CategoryListView.as_view(), name='categories_index'),
    path('create/', views.CategoryCreateView.as_view(), name='category_create'),
    path(
        '<int:pk>/update/',
        views.CategoryUpdateView.as_view(),
        name='category_update'
    ),
    path(
        '<int:pk>/delete/',
        views.CategoryDeleteView.as_view(),
        name='category_delete'
    ),
]