from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordChangeView, PasswordResetConfirmView

from django.views.generic import CreateView, ListView
from .forms import *

from .models import Profile
from posutochno.models import Kvartiri

from django.urls import reverse, reverse_lazy


class UserCreationForm(CreateView):
    form_class = UserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')

        user = authenticate(
            self.request,
            username=username,
            password=password
        )
        login(request=self.request, user=user)
        return response


class ProfileView(ListView):
    model = Kvartiri
    template_name = 'users/profile.html'
    context_object_name = 'kvartiri'


class ResetPassword(PasswordResetView):
    template_name = 'users/password_reset_form.html'
    success_url = reverse_lazy('reset_password_confirm')


class ResetPasswordConfirm(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'


class ResetPasswordDone(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'


class ChangePassword(PasswordChangeView):
    template_name = 'users/password_change_form.html'
