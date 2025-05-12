from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from core.forms import CustomUserCreationForm, CustomLoginForm
from django.urls import reverse_lazy
from django.contrib.auth import login


class CustomLoginView(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True
    form_class = CustomLoginForm

    def get_success_url(self):
        """Handle the 'next' parameter for redirection"""
        return self.request.GET.get('next', reverse_lazy('dashboard'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        return context


class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'auth/signup.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        """Automatically log in the user after signup"""
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
