from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Dashboard'
        return context


class AlbaniaMapView(TemplateView):
    template_name = 'map/albania_map.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # You can add any context data needed for your map here
        return context
