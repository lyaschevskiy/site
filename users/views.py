from django.contrib.auth.views import LoginView, PasswordResetView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib import auth
from common.views import TitleMixin
from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm, UserForgotPasswordForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from users.models import User
from products.models import Basket


class UserLoginView(TitleMixin, LoginView):
    template_name = 'registration/login.html'
    form_class = UserLoginForm
    title = 'Store - Авторизация'


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегестрированы!'
    title = 'Store - Регистрация'


class UserProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'registration/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Store - Личный кабинет'
        context['baskets'] = Basket.objects.filter(user_id=context['user'].id)
        return context

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


class UserForgotPasswordView(SuccessMessageMixin, PasswordResetView):
    model = User
    form_class = UserForgotPasswordForm
    template_name = 'registration/password_reset_form.html'
    title = 'Store - восстановить пароль'


def user_password_reset_done_view(request: HttpRequest) -> HttpResponse:
    return render(request, "registration/password_reset_done.html")

# class UserPasswordResetDoneView(SuccessMessageMixin, PasswordResetDoneView):
#     model = User
#     form_class = UserForgotPasswordForm
#     template_name = 'registration/password_reset_done.html'
#     title = 'Store - проверьте почту'
