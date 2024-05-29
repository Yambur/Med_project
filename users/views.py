import secrets

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from django.views import View
from django.views.generic import CreateView, UpdateView

from config import settings
from med.services import send_new_password, StileFormMixin
from users.forms import RegisterForm, UserForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='Поздравляем с регистрацией',
            message='Вы зарегались на нашей платформе!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
            )
        return super().form_valid(form)


class UserUpdateView(LoginRequiredMixin, UpdateView, StileFormMixin):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


"""class VerifyCodeView(View, StileFormMixin):
    template_name = 'users/verify_code.html'
    success_url = reverse_lazy('med:base')

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        verify_code = request.POST.get('verify_code')
        user = User.objects.filter(verify_code=verify_code).first()
        if user:
            user.is_verified = True
            user.is_active = True
            user.save()
            return redirect('users:login')
        else:
            return redirect('users:register')"""


"""@login_required
def get_new_password(request):
    new_password = ''.join([str(secrets.token_urlsafe(5))])
    request.user.set_password(new_password)
    request.user.save()
    send_new_password(request.user.email, new_password)
    return redirect(reverse('users:login'))"""
