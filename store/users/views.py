from typing import Any

from common.views import TitleMixin
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from products.models import Basket
from users.models import EmailVerification, User

from .forms import UserLoginForm, UserProfileForm, UserRegistrationForm


class UserLoginView(TitleMixin, LoginView):
    template_name = "users/login.html"
    form_class = UserLoginForm
    title = "Store - Авторизация"


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")
    success_message = "Поздравляем! Вы зарегистрированы!"
    title = "Store - Регистрация"


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = "users/profile.html"

    def get_success_url(self) -> str:
        return reverse_lazy("users:profile", args=(self.object.id,))

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(UserProfileView, self).get_context_data()
        context["title"] = "Store - Профиль"
        context["baskets"] = Basket.objects.filter(user=self.object)
        return context


class EmailVerficationView(TitleMixin, TemplateView):
    title = 'Ваша учетная запись успешно подтверждена!'
    template_name = 'users/email_verification.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        code = kwargs.get('code')
        user = User.objects.get(email=kwargs['email'])
        email_verifications = EmailVerification.objects.filter(user=user, code=code)
        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super(EmailVerficationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))












