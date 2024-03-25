from django.contrib.auth.decorators import login_required

from django.urls import path
from users.views import UserLoginView, UserRegistrationView, UserProfileView, logout, UserForgotPasswordView, \
    user_password_reset_done_view

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),
    path('logout/', logout, name='logout'),

    path('password-reset/', UserForgotPasswordView.as_view(), name='password_reset'),
    path('password-reset/done/', user_password_reset_done_view, name='password_reset_done'),
    # path('password-reset/done/', UserPasswordResetDoneView.as_view(), name='password_reset_done'),

    # path('password-reset/done/',
    #      PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"),
    #      name='password_reset_done'),

    # path('password-reset/',
    #      PasswordResetView.as_view(
    #          template_name="registration/password_reset_form.html",
    #          title='Store - пароль',
    #      ),
    #      name='password_reset'),
    #
    # path('password-reset/done/',
    #      PasswordResetDoneView.as_view(
    #          template_name="registration/password_reset_done.html",
    #          title='Store - пароль',
    #      ),
    #      name='password_reset_done'),

]
