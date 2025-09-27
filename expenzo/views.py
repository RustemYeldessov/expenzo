from django.shortcuts import render
from django.views import View
from django.contrib import messages


class IndexView(View):
    def get(self, request):
        if request.session.pop("just_logged_in", False):
            messages.success(request, "Вы авторизованы")
        return render(request, "index.html")