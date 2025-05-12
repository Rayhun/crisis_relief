from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True
    # form_class = CustomLoginForm  # Uncomment if using custom form

    def get_success_url(self):
        """Handle the 'next' parameter for redirection"""
        return self.request.GET.get('next', reverse_lazy('home'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        return context
