from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from Affected.models.event import Event
from core.models import User


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.filter(is_active=True)
        context['user_type'] = {
            'org': user.filter(user_type='org'),
            'volunteers': user.filter(user_type='volunteers'),
            'donors': user.filter(user_type='donors'),
            'affected': user.filter(user_type='affected'),
        }
        context['title'] = 'Dashboard'
        return context


class AlbaniaMapView(TemplateView):
    template_name = 'map/albania_map.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = Event.objects.exclude(status='closed').order_by('-created_at')
        print(event)
        context['events'] = event
        return context
