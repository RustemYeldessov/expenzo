import logging

from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.utils.translation import gettext_lazy as _

from .forms import UserCreateForm, UserLoginForm, UserRegistrationForm, UserUpdateForm


logger = logging.getLogger(__name__)
User = get_user_model()


class UsersListView(ListView):
    model = User
    template_name = "users/index.html"
    context_object_name = "users"


class UsersCreateView(CreateView, SuccessMessageMixin):
    model = User
    template_name = "users/create.html"
    form_class = UserCreateForm
    success_url = reverse_lazy("login")
    success_message = _("User created successfully")