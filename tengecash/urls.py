from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import IndexView

urlpatterns = [
    path("admin/", admin.site.urls),

    path("users/", include(("tengecash.users.urls", "users"), namespace="users")),
    path("categories/", include(("tengecash.categories.urls", "categories"), namespace="categories")),
    path("sections/", include(("tengecash.sections.urls", "sections"), namespace="sections")),
    path("expenses/", include(("tengecash.expenses.urls", "expenses"), namespace="expenses")),
    path("analytics/", include(("tengecash.analytics.urls", "analytics"), namespace="analytics")),

    path("", IndexView.as_view(), name='index'),

    path('api-auth/', include('rest_framework.urls'))
]
