import logging

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.translation import gettext_lazy as _

from .forms import UserCreateForm, UserLoginForm, UserUpdateForm


logger = logging.getLogger(__name__)
User = get_user_model()


class UserListView(ListView):
    model = User
    template_name = "users/index.html"
    context_object_name = "users"


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    template_name = "users/create.html"
    form_class = UserCreateForm
    success_url = reverse_lazy("users:login")
    success_message = _("User created successfully")


class UserUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    SuccessMessageMixin,
    UpdateView
):
    model = User
    template_name = "users/update.html"
    form_class = UserUpdateForm
    success_url = reverse_lazy("users:login")
    success_message = _("User updated successfully")

    # Проверка на то, является ли залогиненный пользователь тем,
    # чьи данные обновляются 👇
    def test_func(self):
        return self.request.user == self.get_object()

    # Если не прошла проверка пользователя
    def handle_no_permission(self):
        # 1. Flash-сообщение
        messages.error(
            self.request,
            _("You do not have permission to perform this action")
        )
        # 2. Редирект на страницу со списком пользователей
        return redirect("users:index")


class UserDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    SuccessMessageMixin,
    DeleteView
):
    model = User
    template_name = "users/delete.html"
    success_url = reverse_lazy("users:index")
    success_message = _("User deleted successfully")

    def test_func(self):
        return self.request.user == self.get_object()

    # Более сложный handle_no_permission разделяет причины отказа:
    # юзер не залогинен / юзер пытается удалить чужой аккаунт
    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.error(
                self.request,
                _("You are not logged in! Please log in")
            )
            return super().handle_no_permission()
        messages.error(
            self.request,
            _("You do not have permission to perform this action")
        )
        return redirect("users:index")

    # post + ProtectedError защищает целостность базы данных от случайного удаления важного.
    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(
                request,
                _("It is impossible to delete the user \
                because it is being used")
            )
            return redirect(self.success_url)


class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = UserLoginForm
    template_name = "users/login.html"
    redirect_authenticated_user = True

    def form_valid(self, form):
        # Сначала выполняем стандартный вход и записывает результат в переменную
        response = super().form_valid(form)
        # Пока редирект еще не улетел в браузер, мы успеваем «подбросить» в сессию сообщение об успехе
        messages.success(self.request, _("You are logged in"))
        # Помечаем в сессии пользователя, что он только что залогинился
        self.request.session["just_logged_in"] = True
        return response

    def get_success_url(self):
        return reverse_lazy("index")


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("users:login")

    def post(self, request, *args, **kwargs):
        messages.success(request, _("You are logged out"))
        return super().post(request, *args, **kwargs)
