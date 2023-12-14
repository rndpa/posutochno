
from django.contrib.auth import views as auth_views
from django.urls import path

from users.views import *

urlpatterns = [
    path('регистрация/', UserCreationForm.as_view(), name='register'),
    path('профиль/', ProfileView.as_view(), name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('сброс-пароля/', ResetPassword.as_view(), name='reset_password'),
    path('подтверждение-сброса-пароля/', ResetPasswordConfirm.as_view(), name='reset_password_confirm'),
    path('сброс-пароля-успешно/', ResetPasswordDone.as_view(), name='reset_password_done'),
    path('смена-пароля/', ChangePassword.as_view(), name='change_password'),
]
