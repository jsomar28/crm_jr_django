from xml.parsers.expat import model

from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import SecureLoginForm, User
from django.views.generic import CreateView, ListView, TemplateView
from django.contrib import messages
from .forms import SecureSignupForm




class DashboardView(LoginRequiredMixin, TemplateView): 
    template_name = 'dashboard.html'

class SecureLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = SecureLoginForm
    redirect_authenticated_user = True


class SignupView(CreateView):
    form_class = SecureSignupForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        
        messages.success(self.request, "Cuenta creada correctamente.")
        return super().form_valid(form)


class SecureLogoutView(LoginRequiredMixin, View):

    def post(self, request):
        logout(request)
        messages.success(request, "Sesión cerrada correctamente.")
        return redirect('login')




class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'
    success_url = reverse_lazy('user_list')

    def get_queryset(self):
        return User.objects.all() 