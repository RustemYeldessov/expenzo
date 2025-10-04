from django.urls import path
from . import views

urlpatterns = [
    path('', views.SectionListView.as_view(), name='sections_index'),
    path('create/', views.SectionCreateView.as_view(), name='sections_create'),
    path('<int:pk>/update/', views.SectionUpdateView.as_view(), name='sections_update'),
    path('<int:pk>/delete/', views.SectionDeleteView.as_view(), name='sections_delete'),
]