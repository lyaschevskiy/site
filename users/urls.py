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
    path('password-reset/done/', user_password_reset_done_view, name='password_reset_done')

]
